# Change Log
Format based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]
### Added
* Support for fetching time series for multiple IOT fields via `IotService.get_time_series_for_fields` ([#52](https://github.com/ndustrialio/contxt-sdk-python/pull/52))
* Support for new Health API via `HealthService` class ([#55](https://github.com/ndustrialio/contxt-sdk-python/pull/55))
* Packaged type information ([PEP 561](https://www.python.org/dev/peps/pep-0561/)) with marker file `py.typed`

### Changed
* Removed unnecessary dependencies, `tzlocal` and `argcomplete`
* Update all models to use dataclasses ([#57](https://github.com/ndustrialio/contxt-sdk-python/pull/57))

### Fixed
* API call for `ContxtService.create_organization` now sends new `slug` parameter ([#54](https://github.com/ndustrialio/contxt-sdk-python/pull/54))
