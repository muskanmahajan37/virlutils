# -*- coding: utf-8 -*-
import click
import tabulate


def lab_list_table(labs, cached_labs=None):
    click.secho("Running Labs", fg="green")
    print_labs(labs)
    if cached_labs:
        click.secho("Cached Labs", fg="yellow")
        print_labs(cached_labs)


def print_labs(labs):
    table = list()
    headers = ["ID", "Title", "Description", "Status", "Nodes", "Links", "Interfaces"]
    for lab in labs:
        tr = list()
        tr.append(lab.id)
        tr.append(lab.title)
        tr.append(lab.description)
        status = lab.state()
        stats = lab.statistics
        if status == "BOOTED":
            color = "green"
        elif status in {"STARTED", "QUEUED"}:
            color = "yellow"
        else:
            color = "red"
        tr.append(click.style(status, fg=color))
        tr.append(stats["nodes"])
        tr.append(stats["links"])
        tr.append(stats["interfaces"])
        table.append(tr)
    # wrap the output in this try/except block as some terminals
    # may have problem with the 'fancy_grid'
    try:
        click.echo(tabulate.tabulate(table, headers, tablefmt="fancy_grid"))
    except UnicodeEncodeError:
        click.echo(tabulate.tabulate(table, headers, tablefmt="grid"))
