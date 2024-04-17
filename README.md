# Authzed Python Client

[![PyPI](https://img.shields.io/pypi/v/authzed?color=%23006dad)](https://pypi.org/project/authzed)
[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0.html)
[![Build Status](https://github.com/authzed/authzed-py/workflows/Test/badge.svg)](https://github.com/authzed/authzed-py/actions)
[![Mailing List](https://img.shields.io/badge/email-google%20groups-4285F4)](https://groups.google.com/g/authzed-oss)
[![Discord Server](https://img.shields.io/discord/844600078504951838?color=7289da&logo=discord "Discord Server")](https://discord.gg/jTysUaxXzM)
[![Twitter](https://img.shields.io/twitter/follow/authzed?color=%23179CF0&logo=twitter&style=flat-square)](https://twitter.com/authzed)

This repository houses the Python client library for Authzed.

[Authzed] is a database and service that stores, computes, and validates your application's permissions.

Developers create a schema that models their permissions requirements and use a client library, such as this one, to apply the schema to the database, insert data into the database, and query the data to efficiently check permissions in their applications.

Supported client API versions:

- [v1](https://docs.authzed.com/reference/api#authzedapiv1)

You can find more info on each API on the [Authzed API reference documentation].
Additionally, Protobuf API documentation can be found on the [Buf Registry Authzed API repository].

See [CONTRIBUTING.md] for instructions on how to contribute and perform common tasks like building the project and running tests.

[Authzed]: https://authzed.com
[Authzed API Reference documentation]: https://docs.authzed.com/reference/api
[Buf Registry Authzed API repository]: https://buf.build/authzed/api/docs/main
[CONTRIBUTING.md]: CONTRIBUTING.md

## Getting Started

We highly recommend following the **[Protecting Your First App]** guide to learn the latest best practice to integrate an application with Authzed.

If you're interested in examples of a specific version of the API, they can be found in their respective folders in the [examples directory].

[Protecting Your First App]: https://docs.authzed.com/guides/first-app
[examples directory]: /examples

## Basic Usage

### Installation

This project is packaged as the wheel `authzed` on the [Python Package Index].

If you are using [pip], the command to install the library is:

```sh
pip install authzed
```

[Python Package Index]: https://pypi.org/project/authzed
[pip]: https://pip.pypa.io

### Initializing a client

With the exception of [gRPC] utility functions found in `grpcutil`, everything required to connect and make API calls is located in a module respective to API version.

In order to successfully connect, you will have to provide a [Bearer Token] with your own API Token from the [Authzed dashboard] in place of `t_your_token_here_1234567deadbeef` in the following example:

[grpc]: https://grpc.io
[Bearer Token]: https://datatracker.ietf.org/doc/html/rfc6750#section-2.1
[Authzed Dashboard]: https://app.authzed.com

```py
from authzed.api.v1 import Client
from grpcutil import bearer_token_credentials


client = Client(
    "grpc.authzed.com:443",
    bearer_token_credentials("t_your_token_here_1234567deadbeef"),
)
```

### Performing an API call

```py
from authzed.api.v1 import (
    CheckPermissionRequest,
    CheckPermissionResponse,
    ObjectReference,
    SubjectReference,
)


post_one = ObjectReference(object_type="blog/post", object_id="1")
emilia = SubjectReference(object=ObjectReference(
    object_type="blog/user",
    object_id="emilia",
))

# Is Emilia in the set of users that can read post #1?
resp = client.CheckPermission(CheckPermissionRequest(
    resource=post_one,
    permission="reader",
    subject=emilia,
))
assert resp.permissionship == CheckPermissionResponse.PERMISSIONSHIP_HAS_PERMISSION
```
