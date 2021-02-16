# Quickstart

## Login

To access any Contxt API, first login with your Contxt credentials:

```sh
contxt auth login
```

This will open a browser window, ask you to login (if not already), and confirm a code. If this succeeds, you should see something like `Your device is now connected.`

## Usage

The CLI's general usage pattern is:

```sh
contxt [entity] [action]
```

For example, to _get_ all _orgs_:

```sh
contxt orgs get
```

See all supported commands [here](./commands.md).
