#!/usr/bin/env python3
"""
PDF 提取工具 - 使用 pdfplumber 快速提取

使用方式：
    python extract_pdf.py <pdf_path> [--pages 1-15]

示例：
    python extract_pdf.py "raw/books/book.pdf"
    python extract_pdf.py "raw/books/book.pdf" --pages 1-15
"""

import sys
import argparse
import pdfplumber
from pathlib import Path


def extract_with_pdfplumber(pdf_path, pages=None):
    """使用 pdfplumber 提取（快速，本地）"""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            total_pages = len(pdf.pages)

            # 如果用户指定了页码范围，直接提取
            if pages:
                start, end = map(int, pages.split('-'))
                page_range = range(start - 1, min(end, total_pages))
                text_parts = []
                for i in page_range:
                    page_text = pdf.pages[i].extract_text()
                    if page_text:
                        text_parts.append(f"=== 第 {i+1} 页 ===\n{page_text}\n")
                result = '\n'.join(text_parts)
            else:
                # 智能提取：两步法
                # 第一步：扫描前 10 页，找到"目录"关键词
                toc_start = None
                for i in range(min(10, total_pages)):
                    page_text = pdf.pages[i].extract_text()
                    if page_text and ('目录' in page_text or '目 录' in page_text or 'CONTENTS' in page_text.upper()):
                        toc_start = i
                        print(f"找到目录起始页：第 {i+1} 页", file=sys.stderr)
                        break

                if toc_start is None:
                    toc_start = 0
                    print("未找到目录关键词，从第 1 页开始提取", file=sys.stderr)

                # 第二步：从目录页开始提取 10 页
                text_parts = []
                for i in range(toc_start, min(toc_start + 10, total_pages)):
                    page_text = pdf.pages[i].extract_text()
                    if page_text:
                        text_parts.append(f"=== 第 {i+1} 页 ===\n{page_text}\n")

                result = '\n'.join(text_parts)

            # 如果提取内容太少，返回错误信息
            if len(result.strip()) < 100:
                return None

            return result

    except Exception as e:
        print(f"提取失败: {e}", file=sys.stderr)
        return None


def main():
    parser = argparse.ArgumentParser(description='PDF 提取工具')
    parser.add_argument('pdf_path', help='PDF 文件路径')
    parser.add_argument('--pages', help='页码范围，如 1-15')

    args = parser.parse_args()

    # 检查文件是否存在
    if not Path(args.pdf_path).exists():
        print(f"错误：文件不存在 {args.pdf_path}", file=sys.stderr)
        sys.exit(1)

    # 使用 pdfplumber 提取
    print("使用 pdfplumber 提取...", file=sys.stderr)
    result = extract_with_pdfplumber(args.pdf_path, args.pages)

    # 输出结果（使用 UTF-8 编码）
    if result:
        sys.stdout.buffer.write(result.encode('utf-8'))
    else:
        print("提取失败：内容为空或文件格式不支持", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
