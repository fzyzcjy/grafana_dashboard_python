# grafana-dashboard-python

Write Grafana dashboards in Python, without losing thousands of dashboards in the zoo (tiny utility)

## Introduction

Grafana's [official best practice](https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/best-practices/#high---optimized-use) recommends to use scripts to generate the dashboards, instead of creating it in GUI manually. This avoids a lot of repetition, and also ensures consistency.

[Grafanalib](https://github.com/weaveworks/grafanalib) is a library for that purpose, and I have enjoyed it in my system. However, I also want to use (download and customize) the dashboards already built by other people (https://grafana.com/grafana/dashboards/). Therefore, I create this tiny utility.

## Stability / bugs / tests

Firstly, it works well for my own cases, and I have ensured the parts that I use looks correct. However, there are definitely rough edges that I have not manually optimized, since Grafana's auto-generated schema will not solve everything.

As you know, my philosophy is that, if a tool that I use internally may also be useful for others, I will open source it to help people - that's why this tiny utility is on GitHub. However, I am too busy recently, and thus do not have that much time to cover every rough edge of Grafana features that I have not used.

If you see a bug, feel free to create an issue or PR, and I usually reply quickly (within minutes or hours, except sleeping). From my experience, it is very trivial to solve the hard edges. Anyway, this is nothing but a series of Pydantic models with almost *no logic*. How can it have hard-to-fix bugs? ;)

More importantly, you can always check the output JSON to see whether there is an unexpected output. For example, in my own workflow, I let Git track the JSON. Then, if anything changes, I have a clear diff.

## Relation with Grafanalib

I do hope that I can simply PR to Grafanalib and add the "convert any JSON into Python" feature. However, in my humble opinion it is quite hard: Grafanalib's API differs a lot from Grafana's JSON API. Therefore, though I can easily convert JSON to Python dict or object constructor, it is time-consuming to further convert it into valid Grafanalib code.
