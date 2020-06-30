#!/usr/bin/python3
import argparse
import logging
import pathlib
from datetime import date
from os import listdir, mkdir, path
from typing import List, Optional, Set

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)

POST_TEMPLATE = """---
layout: post
title: "{title}"
tags: {tags} 
date: {date}
---
"""

TAG_FILE_TEMPLATE = """---
layout: tag_page
tag: {tag} 
permalink: /tags/{tag}
---
"""


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.set_defaults(which="default")
    subparsers = parser.add_subparsers()
    post = subparsers.add_parser("new_post", help="create new post")
    post.add_argument("title", help="the title of the new post")
    post.add_argument(
        "--draft",
        action="store_true",
        default=False,
        help=("if this variable is set to true, the new post will be put to _draft"),
    )
    post.add_argument(
        "--tags", type=str, nargs="+", help="tags gonna be added to the created post"
    )
    post.add_argument(
        "--override", action="store_true", default=False, help="override existing post"
    )
    post.set_defaults(which="new_post")
    parser.add_argument(
        "--update_tags",
        action="store_true",
        default=False,
        help="update tag files based existing posts",
    )

    return parser


def get_root() -> str:
    return pathlib.Path(__file__).parent.absolute()


def get_tags_from_post(file_path: str) -> Set[str]:
    with open(file_path, "r") as f:
        for line in f.readlines():
            if line.startswith("tags:"):
                return {tag for tag in line.split(":")[1].strip().split(" ")}
    return {}


def update_tags(tags: Optional[Set[str]] = None) -> None:
    if tags is None:
        tags = get_all_tags_from_posts()

    tags_dir = get_tags_dir()
    for tag in tags:
        tag_file_path = path.join(tags_dir, tag + ".md")
        if not path.exists(tag_file_path):
            with open(tag_file_path, "w") as f:
                f.write(TAG_FILE_TEMPLATE.format(tag=tag))
            logging.info(f"Create tag file:{tag_file_path}")


def get_all_tags_from_posts() -> Set[str]:
    posts_dir = get_posts_dir()
    tags = set()
    for f in listdir(posts_dir):
        file_path = path.join(posts_dir, f)
        if path.isfile(file_path):
            tags.update(get_tags_from_post(file_path))
    return tags


def get_tags_dir() -> str:
    tags_dir = path.join(get_root(), "tags")
    if path.exists(tags_dir):
        mkdir(tags_dir)
    return tags_dir


def get_posts_dir() -> str:
    posts_dir = path.join(get_root(), "_posts")
    if path.exists(posts_dir):
        mkdir(posts_dir)
    return posts_dir


def get_drafts_dir() -> str:
    drafts_dir = path.join(get_root(), "_drafts")
    if path.exists(drafts_dir):
        mkdir(drafts_dir)
    return drafts_dir


def create_post(
    title: str, is_draft: bool = False, tags: List[str] = [], override: bool = False
) -> None:
    cur_date = str(date.today())
    file_name = cur_date + "-" + title.lower().replace(" ", "-") + ".md"
    file_path = ""
    if is_draft:
        file_path = path.join(get_drafts_dir(), file_name)
    else:
        file_path = path.join(get_posts_dir(), file_name)

    if path.exists(file_path) and not override:
        raise ValueError(f"Try create a pre-existed post[{file_path}]")

    with open(file_path, "w") as f:
        f.write(POST_TEMPLATE.format(title=title, tags=" ".join(tags), date=cur_date))
    logging.info(f"Create post file:{file_path}")
    if tags:
        update_tags(set(tags))


def main():
    parser = create_parser()
    args = parser.parse_args()
    if args.which == "new_post":
        create_post(
            args.title, is_draft=args.draft, tags=args.tags, override=args.override
        )
    if args.update_tags:
        update_tags()


if __name__ == "__main__":
    main()
