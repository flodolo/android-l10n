#!/usr/bin/env python3

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import random


def main():
    file = "mozilla-mobile/focus-android/app/src/main/res/values/strings.xml"
    with open(file, "r") as f:
        lines = f.readlines()

    r = int(random.random() * 1000)
    lines[8] = f'    <string name="action_cancel">Cancel {r}</string>\n'

    lines.insert(
        len(lines) - 1, f'    <string name="action_cancel_{r}">Firefox test</string>\n'
    )

    with open(file, "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main()
