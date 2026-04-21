#!/usr/bin/env python3
"""
Wiki搜索工具
支持关键词搜索、基于frontmatter的过滤和简单的相关性排序
"""

import os
import re
import argparse
import yaml
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any
import sys

class WikiSearcher:
    def __init__(self, wiki_path: str = "wiki"):
        """初始化搜索器"""
        self.wiki_path = Path(wiki_path)
        if not self.wiki_path.exists():
            raise ValueError(f"Wiki路径不存在: {wiki_path}")

        self.all_files = []
        self._scan_wiki()

    def _scan_wiki(self):
        """扫描wiki目录中的所有markdown文件"""
        for root, dirs, files in os.walk(self.wiki_path):
            # 跳过隐藏目录
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            for file in files:
                if file.endswith('.md') and file not in ['log.md', 'index.md']:
                    filepath = Path(root) / file
                    self.all_files.append(filepath)

    def _parse_frontmatter(self, content: str) -> Dict[str, Any]:
        """解析markdown文件的frontmatter"""
        frontmatter = {}
        frontmatter_pattern = r'^---\s*\n(.*?)\n---\s*\n'
        match = re.search(frontmatter_pattern, content, re.DOTALL)

        if match:
            try:
                frontmatter = yaml.safe_load(match.group(1))
                if frontmatter is None:
                    frontmatter = {}
            except yaml.YAMLError:
                frontmatter = {}

        return frontmatter

    def _extract_title(self, content: str) -> str:
        """从内容中提取标题（第一个一级标题）"""
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if title_match:
            return title_match.group(1).strip()
        return ""

    def _calculate_relevance(self, content: str, keyword: str, frontmatter: Dict[str, Any]) -> float:
        """计算内容和关键词的相关性分数"""
        score = 0.0

        # 转换为小写便于比较
        content_lower = content.lower()
        keyword_lower = keyword.lower()

        # 标题匹配（最高权重）
        title = self._extract_title(content)
        if keyword_lower in title.lower():
            score += 10.0

        # Frontmatter匹配
        for key, value in frontmatter.items():
            if isinstance(value, str) and keyword_lower in value.lower():
                score += 5.0
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, str) and keyword_lower in item.lower():
                        score += 3.0

        # 内容匹配
        matches = re.findall(r'\b' + re.escape(keyword_lower) + r'\b', content_lower)
        score += len(matches) * 0.5

        # 非精确匹配
        if keyword_lower in content_lower:
            score += 1.0

        return score

    def search(self, keyword: str, limit: int = 20, min_score: float = 0.1) -> List[Dict[str, Any]]:
        """搜索wiki内容"""
        results = []

        for filepath in self.all_files:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 解析frontmatter
                frontmatter = self._parse_frontmatter(content)

                # 计算相关性
                relevance = self._calculate_relevance(content, keyword, frontmatter)

                if relevance >= min_score:
                    # 提取标题
                    title = self._extract_title(content)
                    if not title and 'title' in frontmatter:
                        title = frontmatter.get('title', '')

                    # 提取摘要（前200个字符）
                    content_without_frontmatter = re.sub(r'^---\s*\n.*?\n---\s*\n', '', content, flags=re.DOTALL)
                    lines = content_without_frontmatter.strip().split('\n')
                    summary_lines = []
                    for line in lines:
                        if line.strip() and not line.strip().startswith('#'):
                            summary_lines.append(line.strip())
                            if sum(len(l) for l in summary_lines) >= 200:
                                break

                    summary = ' '.join(summary_lines)[:200] + '...'

                    # 查找关键词出现的上下文
                    contexts = []
                    lines_with_numbers = content_without_frontmatter.split('\n')
                    for i, line in enumerate(lines_with_numbers[:50]):  # 只检查前50行
                        if keyword.lower() in line.lower():
                            context_line = min(max(0, i-1), len(lines_with_numbers)-1)
                            context = lines_with_numbers[context_line:i+2]
                            contexts.append(' | '.join([l.strip() for l in context if l.strip()]))

                    result = {
                        'file': str(filepath),
                        'title': title or os.path.basename(filepath),
                        'relevance': relevance,
                        'summary': summary,
                        'contexts': contexts[:3],  # 最多3个上下文
                        'type': frontmatter.get('type', 'unknown'),
                        'updated': frontmatter.get('updated', ''),
                        'tags': frontmatter.get('tags', []),
                        'link': f"[[{filepath.relative_to(self.wiki_path).with_suffix('')}]]"
                    }

                    results.append(result)

            except Exception as e:
                print(f"警告：处理文件 {filepath} 时出错: {e}", file=sys.stderr)
                continue

        # 按相关性排序
        results.sort(key=lambda x: x['relevance'], reverse=True)

        return results[:limit]

    def search_by_type(self, page_type: str) -> List[Dict[str, Any]]:
        """按页面类型搜索"""
        typed_results = []

        for filepath in self.all_files:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                frontmatter = self._parse_frontmatter(content)
                if frontmatter.get('type') == page_type:
                    title = self._extract_title(content)
                    typed_results.append({
                        'file': str(filepath),
                        'title': title or os.path.basename(filepath),
                        'type': page_type,
                        'updated': frontmatter.get('updated', ''),
                        'link': f"[[{filepath.relative_to(self.wiki_path).with_suffix('')}]]"
                    })

            except Exception as e:
                continue

        return typed_results

    def get_stats(self) -> Dict[str, Any]:
        """获取wiki统计信息"""
        stats = {
            'total_files': len(self.all_files),
            'by_type': {},
            'recent_updates': []
        }

        # 按类型统计
        for filepath in self.all_files:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                frontmatter = self._parse_frontmatter(content)
                page_type = frontmatter.get('type', 'unknown')
                stats['by_type'][page_type] = stats['by_type'].get(page_type, 0) + 1

                # 收集最近更新
                updated = frontmatter.get('updated')
                if updated:
                    try:
                        update_date = datetime.strptime(updated, '%Y-%m-%d')
                        stats['recent_updates'].append({
                            'file': str(filepath),
                            'updated': updated,
                            'date': update_date
                        })
                    except ValueError:
                        pass

            except Exception:
                continue

        # 按日期排序最近更新
        stats['recent_updates'].sort(key=lambda x: x['date'], reverse=True)
        stats['recent_updates'] = stats['recent_updates'][:10]  # 最近10个

        return stats

def main():
    parser = argparse.ArgumentParser(description="Wiki搜索工具")
    parser.add_argument("keyword", nargs="?", help="搜索关键词")
    parser.add_argument("--path", default="wiki", help="wiki路径")
    parser.add_argument("--limit", type=int, default=20, help="结果数量限制")
    parser.add_argument("--min-score", type=float, default=0.1, help="最小相关性分数")
    parser.add_argument("--type", help="按页面类型过滤")
    parser.add_argument("--stats", action="store_true", help="显示wiki统计信息")
    parser.add_argument("--verbose", "-v", action="store_true", help="详细输出")

    args = parser.parse_args()

    try:
        searcher = WikiSearcher(args.path)

        if args.stats:
            stats = searcher.get_stats()
            print(f"\n[统计] Wiki统计信息")
            print(f"总文件数: {stats['total_files']}")
            print("\n按类型分布:")
            for page_type, count in stats['by_type'].items():
                print(f"  {page_type}: {count}")

            print(f"\n最近更新:")
            for update in stats['recent_updates'][:5]:
                print(f"  {update['updated']} - {update['file']}")

        elif args.type:
            results = searcher.search_by_type(args.type)
            print(f"\n[搜索] 类型 '{args.type}' 的页面 ({len(results)} 个):")
            for i, result in enumerate(results, 1):
                print(f"{i}. {result['title']}")
                if args.verbose:
                    print(f"   文件: {result['file']}")
                    print(f"   类型: {result['type']}")
                    print(f"   链接: {result['link']}")
                    print()

        elif args.keyword:
            results = searcher.search(args.keyword, args.limit, args.min_score)
            print(f"\n[搜索] 搜索 '{args.keyword}' 的结果 ({len(results)} 个):")

            for i, result in enumerate(results, 1):
                print(f"\n{i}. {result['title']} (相关性: {result['relevance']:.2f})")
                print(f"   类型: {result['type']}")
                print(f"   摘要: {result['summary']}")
                print(f"   链接: {result['link']}")

                if args.verbose and result['contexts']:
                    print(f"   上下文:")
                    for context in result['contexts'][:2]:
                        print(f"     - {context[:100]}...")

        else:
            parser.print_help()

    except Exception as e:
        print(f"错误: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()