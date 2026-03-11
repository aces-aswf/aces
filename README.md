<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright Contributors to the ACES Project -->

![Academy Color Encoding
System](https://github.com/AcademySoftwareFoundation/artwork/blob/main/projects/aces/horizontal/color/aces-horizontal-color.png)

# Academy Color Encoding System

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## How to use this repository

This repository provides a structured and organized way to track and manage ACES release bundles and their associated modular components, which are hosted in the following subrepositories:

- **aces-core** contains the maths and algorithms that are at the core of the ACES rendering transforms 
- **aces-amf** holds the XSD schema and example files for ACES Metadata File (AMF)
- **aces-input-and-colorspaces** ontains color space definitions and the conversions between them, i.e. to/from ACES2065-1
- **aces-output** transforms with parameters preset to correspond with characteristics of standard or common display configurations
- **aces-look** contains any transforms that serve to modify the default appearance of images through an ACES pipeline

## Tags and Releases

> [!IMPORTANT]
> The HEAD of the `main` branch always reflects the "latest and greatest" state of all submodules. This may include new transforms or changes that have not yet been "bundled". 
>
> Because individual modular components do not affect the core functionality of ACES, they may be updated between official bundles. For consistency, production pipelines and implementations should reference the latest tagged releases.

### Versioning Logic

ACES uses [semantic versioning](https://semver.org/) (**MAJOR.MINOR.PATCH**): 

- **MAJOR**: Significant changes to core ACES algorithms resulting in changest to output pixels.
- **MINOR**: Non-breaking changes of significance (e.g., new backward-compatible functionality).
- **PATCH**: Backward-compatible bug fixes.

### Release bundles

Bundles package the parent repository and all submodules into a ZIP archive. Each bundles is associated with a specific version tag that includes the ACES semantic version plus a **Build Number** (the date the components were collected):

`MAJOR.MINOR.PATCH+YYYY.MM.DD`

> [!IMPORTANT] This repository only contains history for **ACES 2.0 and newer**. The
> git history for earlier ACES versions is [preserved in `aces-dev`](https://github.com/aces-aswf/aces-core/tags), which was relabeled as `aces-core` during the ACES 2 code reorganization.

### Release Cadence

Releases are currently scheduled manually, but the TSC is considering establishing a semi-annual cadence to help implementers better anticipate and schedule ACES updates into their own product release cycles.

## ACES Resources

- Website: <https://acescentral.com>
  - Documentation: <https://docs.acescentral.com>
  - Forum: <https://community.acescentral.com>
- Slack workspace: <https://aswf.slack.com>
  - New users can join via <http://slack.aswf.io>

## Contributing

ACES depends on community participation. Developers, manufacturers, and end users are encouraged to contribute code, bug fixes, documentation, and other technical artifacts.

All contributors must have a signed Contributor License Agreement (CLA) on file to ensure that the project can freely use your contributions. 

See [CONTRIBUTING.md](./CONTRIBUTING.md) for more details.

## Governance

ACES is a project hosted by the [Academy Software Foundation](https://aswf.io). 

See [GOVERNANCE.md](GOVERNANCE.md) for details about how the project operates.

## Reporting Issues

To report a problem, please open an issue. 

- Whenever possible, issues specific to a particular transform or component should be filed using the issue tracker of its containing repository.
- General issues can be filed in this repository's [issue tracker](https://github.com/aces-aswf/aces/issues). 
- For sensitive or security-related issues, do not use the public issue tracker. Instead, refer to [SECURITY.md](SECURITY.md) for details on the project's security policy.

## License

The ACES Project is licensed under the [Apache 2.0 license](./LICENSE).