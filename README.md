<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright Contributors to the ACES Project -->

![Academy Color Encoding
System](https://github.com/AcademySoftwareFoundation/artwork/blob/main/projects/aces/horizontal/color/aces-horizontal-color.png)

# Academy Color Encoding System

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

The Academy Color Encoding System (ACES) is a framework for interchanging
digital image files, managing color workflows and creating masters for delivery
and archiving. ACES is designed to unify color management across the entire
imaging chain, including capture, postproduction, distribution, and preservation, so that
images look consistent and creative intent is maintained.

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

## ACES Project Mission

The Academy Color Encoding System (ACES) aims to provide a standardized, device-independent, and future-proof system for managing color throughout the motion picture and television production pipeline.

ACES aims to:

- provide a common color interchange format (ACES2065-1) to facilitate image interchange and archival
- enable consistent color reproduction from image capture through editing, VFX, grading, mastering, and archiving, regardless of camera, display, or workflow
- preserve creative intent across different display devices and between software and hardware from different vendors
- support long-term archiving of motion picture assets in a format that can be faithfully re-rendered on future display technologies
- recieve wide industry adoption
- foster a healthy and active community

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

### ACES History
This repository only contains history for ACES 2.0 and newer. The git history for earlier ACES versions is [preserved in `aces-dev`](https://github.com/ampas/aces-core/tags), which was relabeled the `aces-core` repository with the reorganization associated with ACES 2.  

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

ACES is a project hosted by the [ASWF](https://aswf.io). See
[GOVERNANCE.md](GOVERNANCE.md) for details about how the project operates.

## Reporting Issues

To report a problem, please open an issue. 

- General issues should be filed in this repository's [issue tracker](https://github.com/ampas/aces/issues). 
- Issues specific to a particular transform or component should be filed in the issue tracker of the corresponding submodule whenever possible.
- For sensitive or security-related issues, do not use the public issue tracker. Instead, refer to [SECURITY.md](SECURITY.md) for details on the project's security policy.

## License

The ACES Project is licensed under the [Apache 2.0 license](./LICENSE).