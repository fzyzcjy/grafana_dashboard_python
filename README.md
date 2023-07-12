# grafana_dashboard_python

[![PyPI](https://img.shields.io/pypi/v/grafana-dashboard)](https://pypi.org/project/grafana-dashboard/)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/c12919fe67ca46f098bf1a57bb8adb1e)](https://app.codacy.com/gh/fzyzcjy/grafana_dashboard_python/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)

Write Grafana dashboards in Python, without losing thousands of dashboards in the zoo

![](doc/logo.svg)

## Introduction

Grafana's [official best practice](https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/best-practices/#high---optimized-use) recommends **using scripts to generate dashboards**, instead of creating it in GUI manually. This avoids a lot of repetition, and also ensures consistency.

[Grafanalib](https://github.com/weaveworks/grafanalib) is a library for that purpose, and I have enjoyed it in my system. However, I also want to **download and customize the dashboards already built by other people** (https://grafana.com/grafana/dashboards/). Therefore, I create this small tool.

In the following sections, I assume you are familiar with Grafanalib, and want to use dashboards in the world.

## Installation

```py
pip install grafana_dashboard
```

## Sample workflow 1: Customize an existing dashboard

### Step 1: Convert standard Grafana dashboard into Python code

To begin with, get your dashboard from wherever you like, such as https://grafana.com/grafana/dashboards/, or your legacy dashboards. Then convert it to Python code:

```py
grafana_dashboard json-to-python --json-path ... --python-path ...
```

Currently, you may need a bit of cleanup for the generated code, mostly add a few `import`s. (Should be automated in future releases.)

### Step 2: Customize it in Python

Since it is nothing but normal Python code, you can customize it freely, and it can be easily made consistent with other dashboards written in Python.

For example, I personally have a few annotations that should be applied to every dashboard, then I can just add `annotations=get_common_annotations()` and that's all - no need to copy-and-paste dozens of lines.

### Step 3: Deploy it

Same as Grafanalib, just convert Python into JSON, and use you favorite approach to send the JSON to Grafana. As for the arguments of the conversion command:

```py
grafana_dashboard python-to-json --python-base-dir ... --python-base-package ... --json-dir ...
```

## Sample workflow 2: Create a dashboard from scratch

Just throw away "step 1" in the sample above :)

## Stability / bugs / tests

Firstly, it works well for my own cases, and I have ensured the parts that I use looks correct. However, there are definitely rough edges that I have not manually optimized, since Grafana's auto-generated schema will not solve everything.

As you know, my philosophy is that, if a tool that I use internally may also be useful for others, I will open source it to help people - that's why this tiny utility is on GitHub. However, I am too busy recently, and thus do not have that much time to cover every rough edge of Grafana features that I have not used.

If you see a bug, feel free to create an issue or PR, and I usually reply quickly (within minutes or hours, except sleeping). From my experience, it is very trivial to solve the hard edges. Anyway, this is nothing but **a series of Pydantic models with almost *no logic***. How can it have hard-to-fix bugs? ;)

More importantly, you can always check the output JSON to see whether there is an unexpected output. For example, in my own workflow, I let Git track the JSON. Then, if anything changes, I have a clear diff.

## Examples

Examples can be found at `/examples`.

## Relation with Grafanalib

Firstly, thank you Grafanlib for the helpful tool!

I do hope that I can simply PR to Grafanalib and add the "convert any JSON into Python" feature. However, in my humble opinion it is quite hard: Grafanalib's API differs a lot from Grafana's JSON API. Therefore, though I can easily convert JSON to Python dict or object constructor, it is time-consuming and error-prone to further convert it into valid Grafanalib code.

## How it works

Pretty simple. When using it, it is nothing but a series of `Pydantic` models, with almost no logic except that. So you are indeed using the serialization and deserialization feature of Pydantic.

As for how the Pydantic code is created: It is generated automatically from Grafana's official [schema](https://github.com/grafana/grok), and then manually tweaked for a better developer experience (e.g. provide more sensible defaults, make types looser). All changes are recorded in a patch file, so the package can be easily upgraded when Grafana upgrades, and always keep the definition accurate.

## Tips

* You can (auto) migrate the JSON to latest `schemaVersion` by importing the JSON into Grafana and download/save JSON from the imported dashboard. Doing so may make your code a bit cleaner.
* If the Python generated from JSON gives weird results, it is trivial to debug: Just compare the newly generated JSON with the original JSON, and fix any noticeable differences.
