<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright Contributors to the ACES Project -->

![Academy Color Encoding
System](https://github.com/AcademySoftwareFoundation/artwork/blob/main/projects/aces/horizontal/color/aces-horizontal-color.png)

# Academy Color Encoding System

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Introduction

The Academy Color Encoding System (ACES) started as an initative led by the
Academy of Motion Picture Arts and Sciences to establish a unified,
device-independent system for managing color throughout motion picture
production. It has found usage in motion pictures, television, animation, VFX,
gaming, immersive media, and related fields. The project’s mission is to enable
predictable, high-quality color reproduction across diverse workflows and
technologies, preserving creative intent while supporting interoperability,
archival needs, and future innovation.

## ACES Project Mission

The Academy Color Encoding System (ACES) aims to provide a standardized,
device-independent, and future-proof system for managing color throughout a
production pipeline.

ACES aims to:

- define and maintain open, standardized encodings and transforms for color
  management
- provide a robust framework to support production, post-production,
  distribution, and archiving
- ensure compatibility with emerging imaging technologies, including high
  dynamic range and wide color gamut
- enable consistent color reproduction from image capture through editing, VFX,
  grading, mastering, and archiving, regardless of hardware or workflow
- support long-term archiving of motion picture assets in a format that can be
  faithfully re-rendered on future display technologies
- promote wide industry adoption
- foster a healthy and active community

## ACES Components

This repository provides a structured and organized way to track and manage
different versions of ACES, along with their associated modular components,
which are separated into subrepositories:

- **aces-core:** 
  - contains the maths and algorithms that are at the core of the ACES rendering
  transforms 
- **aces-amf:** 
  - holds the XSD schema and example files for ACES Metadata File (AMF)
- **aces-input-and-colorspaces:** 
  - contains color space definitions and the conversions between them, i.e.
  to/from ACES2065-1
- **aces-output:** 
  - transforms with parameters preset to correspond with characteristics of
  standard or common display configurations
- **aces-look:** 
  - contains any transforms that serve to modify the default appearance of
  images through an ACES pipeline

## Tags and Releases

ACES uses [semantic versioning](https://semver.org/). The version number of ACES
reflects changes to the ACES core algorithms. 

- **MAJOR.MINOR.PATCH**: Reflects changes to the core ACES algorithms.

A build number denotes the specific collection of modular components (e.g.,
[Input and Color Space
Transforms](https://github.com/ampas/aces-input-and-colorspaces), [Output
Transforms](https://github.com/ampas/aces-output), etc.) in date format.

- **Build Number**: Identifies the specific collection of modular components
  from the submodules - formatted as `+YYYY.MM.DD`

### Modular Components

The modular components of ACES can be updated at any time by the ACES team or by
end users. These components do not affect the core functionality of ACES, which
is why they are not included in the MAJOR.MINOR.PATCH version number.

> [!IMPORTANT]
> This repository only contains history for ACES 2.0 and newer. The git history
for earlier ACES versions is [preserved in
`aces-dev`](https://github.com/ampas/aces-core/tags), which was relabeled as
`aces-core` during a code reorganization associated with the release of ACES 2.  

## ACES Resources

- Website: <https://acescentral.com>
  - Documentation: <https://docs.acescentral.com>
  - Forum: <https://community.acescentral.com>
- Slack workspace: <https://aswf.slack.com>
  - New users can join via <http://slack.aswf.io>

## Contributing

ACES depends on community participation. Developers, manufacturers, and end
users are encouraged to contribute code, bug fixes, documentation, and other
technical artifacts.

All contributors must have a signed Contributor License Agreement (CLA) on file
to ensure that the project can freely use your contributions. 

See [CONTRIBUTING.md](./CONTRIBUTING.md) for more details.

## Governance

ACES is a project hosted by the [Academy Software Foundation](https://aswf.io). 

See [GOVERNANCE.md](GOVERNANCE.md) for details about how the project operates.

## Reporting Issues

To report a problem, please open an issue. 

- Whenever possible, issues specific to a particular transform or component
  should be filed using the issue tracker of its containing repository.
- General issues can be filed in this repository's [issue
  tracker](https://github.com/ampas/aces/issues). 
- For sensitive or security-related issues, do not use the public issue tracker.
  Instead, refer to [SECURITY.md](SECURITY.md) for details on the project's
  security policy.

## License

The ACES Project is licensed under the [Apache 2.0 license](./LICENSE).