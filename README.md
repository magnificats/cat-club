\## Cat Club

Cat how and ranking software!

This will be a frappe app to enable users to manage cat clubs, shows, rings, etc. Currently in the extremely early stages of development. Use at your own peril: expect things to change drastically on a daily basis, and things to break. It is NOT RECOMMENDED for non-developers to use this software at the current moment.

## Frappe

This is an app to be used with Frappe. Consequently, you'll need to install that to test this.

1. Follow the [installation guide](https://frappeframework.com/docs/v14/user/en/installation)
2. Create a [site](https://frappeframework.com/docs/v14/user/en/tutorial/create-a-site)
3. Optionally, configure [nginx](https://frappeframework.com/docs/v14/user/en/bench/guides/setup-production#nginx) (you don't 100% need this, but I find it makes life easier)
4. Assuming your goal is to submit pull requests after fixing things, you will also need to turn on developer mode with "bench set-config -g developer_mode 1". More information [here](https://frappeframework.com/docs/v14/user/en/guides/app-development/how-enable-developer-mode-in-frappe).
5. Install this app with "bench get-app cat_club https://github.com/magnificats/cat-club". More information about apps can be found [here](https://frappeframework.com/docs/v13/user/en/basics/apps)

## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You can download a copy of the GNU General Public License [here](https://www.gnu.org/licenses/gpl-3.0.en.html). 
