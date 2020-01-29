# Change Log
Format based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [1.0.0-beta.10](https://github.com/ndustrialio/contxt-sdk-python/releases/tag/v1.0.0-beta.10) - 2020-01-28

### Added
* Support for fetching time series for multiple IOT fields via `IotService.get_time_series_for_fields` ([#52](https://github.com/ndustrialio/contxt-sdk-python/pull/52))
* Support for new Health API via `HealthService` class ([#55](https://github.com/ndustrialio/contxt-sdk-python/pull/55))
* Support for new IOT V2 API via `IotDataService` class ([#55](https://github.com/ndustrialio/contxt-sdk-python/pull/58))
* Packaged type information ([PEP 561](https://www.python.org/dev/peps/pep-0561/)) with marker file `py.typed`

### Changed
* Removed unnecessary dependencies, `tzlocal` and `argcomplete`
* Update all models to use dataclasses ([#57](https://github.com/ndustrialio/contxt-sdk-python/pull/57))

### Fixed
* API call for `ContxtService.create_organization` now sends new `slug` parameter ([#54](https://github.com/ndustrialio/contxt-sdk-python/pull/54))
