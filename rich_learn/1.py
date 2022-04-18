#!/usr/bin/env python
# -*- coding: utf-8 -*-


from rich import print as rprint

rprint("[italic red]Hello[/italic red] World!", locals())

from rich.console import Console

console = Console()

console.print([1, 2, 3])
console.print("[blue underline]Looks like a link")
console.print(locals())
console.print("MEDUSA", style="white on blue")
