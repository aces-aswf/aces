<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- Copyright Contributors to the ACES Project -->

![Academy Color Encoding
System](https://github.com/AcademySoftwareFoundation/artwork/blob/main/projects/aces/horizontal/color/aces-horizontal-color.png)

# Academy Color Encoding System

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

The **ACES** repository serves as the coordination point for ACES release packages.  
It aggregates the modular component repositories that define the ACES rendering transforms, color space definitions, metadata formats, and related functionality.

Tagged releases in this repository represent official ACES packages, which capture a consistent snapshot of all component repositories at a specific point in time.

## Repository Structure

This repository ("**aces**") tracks ACES release packages and coordinates the modular component repositories listed below:

* [**aces-core**](https://github.com/aces-aswf/aces-core) – Core mathematical models and algorithms used by the ACES rendering transforms.
* [**aces-amf**](https://github.com/aces-aswf/aces-amf) – The schema and example files for the ACES Metadata File (AMF) format.
* [**aces-input-and-colorspaces**](https://github.com/aces-aswf/aces-input-and-colorspaces) – Color space definitions and transforms to and from ACES2065–1.
* [**aces-output**](https://github.com/aces-aswf/aces-output) – Output Transforms configured for common display characteristics and viewing environments.
* [**aces-look**](https://github.com/aces-aswf/aces-look) – Look Transforms that modify the default appearance of images within an ACES pipeline.

> [!NOTE]
> This repository structure was introduced with version 2 and so only contains history for **ACES 2.0 and newer**. The git history for earlier ACES versions is still preserved and can be found in [`aces-core`](https://github.com/aces-aswf/aces-core/tags) 
>
> (`aces-core` is the repository previously named `aces-dev` and was the single repository tracking all ACES components pre-version 2).

## `main` vs Tagged Releases

The `main` branch reflects the latest development state of ACES and its submodules. It points to the most recent commits across the modular component repositories, which may include updates that have not yet been packaged into an ACES release.

Because ACES is composed of multiple modular components, updates can occur between packaged releases. For example, a new camera may contribute an additional Input Transform, or a new Output Transform preset may be introduced for a specific display configuration. These additions may appear in `main` before they are included in a packaged release.

> [!IMPORTANT]
> The `main` branch is the "bleeding edge". Its contents may change as new transforms or updates are merged.

Tagged releases provide a versioned snapshot of this repository and all of its submodules at a specific point in time. These snapshots correspond to official ACES release packages.

>[!TIP]
>**Which should I use?**
>
> * Use `main` if you want the latest development changes and are comfortable integrating updates as they appear.
> * Use a tagged release if you need a stable version suitable for production pipelines or product implementations.

### ACES Versioning

ACES uses [semantic versioning](https://semver.org/) (**MAJOR.MINOR.PATCH**) to indicate updates. 

- **MAJOR** – Significant changes to core ACES algorithms that may result in different output pixel values.
- **MINOR** – Backward-compatible additions or improvements to the ACES system.
- **PATCH** – Backward-compatible fixes or clarifications that do not change intended behavior.

> [!NOTE]
> ACES is intentionally modular. Its components are maintained in separate repositories so that new transforms can be added without affecting the core behavior of the system. The addition of new Input, Output, or Look Transforms therefore does **not** mandate a change to the ACES system version number. Changes to the version number reflect when the core ACES algorithms or their behavior are modified.
 
### Release Packages

Release packages bundle the parent repository and all submodules into a ZIP archive representing an ACES distribution.

Each release is identified by a version tag consisting of the ACES semantic version plus a **build date** indicating when the package was assembled:

```
MAJOR.MINOR.PATCH+YYYY.MM.DD
```

### Release Cadence

Releases are currently scheduled manually. The Technical Steering Committee (TSC) is exploring ways to establish a more predictable release cadence and clearer criteria for what is included in each package. The goal is to help implementers better anticipate and plan ACES updates within their own product release cycles.

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
