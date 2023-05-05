# Incognia Project!
Project for Data Engineering Course (IF997 CIn UFPE)
Professor: Fernando de Paula
Group: Andre Filho; Yves Lawrrence; Victor Ximenes

All logic from the app can be found in either graficos.ipynb and processamento.py

## Proposed Pre-processing Steps:

* Use means/medians in rows with missing integer values
* Delete rows with missing strings
* Attempt to handle non-boolean data in boolean columns
* Delete rows with missing booleans
* Delete rows with missing timestamps

## Proposed Data Transformations:

* timestamp (int) -> weekday (string)

## Proposed New Columns:

* Devices per account (int)
* Wallpapers per device account (float)
* External Download (bool) = root (true) + official store (false)
* Installation on different device? (bool) (count_installation_on_different_devices)

## Things to Consider:

1. What data is important for registration validation?
 * Installed apps from official store?
 * Is it an emulator?
 * Does it have a fake location app?
 * Is the device rooted?
 * Accounts per device
 * Devices per account
 * Day of account access
2. What helps to identify a device?
 * Device ID
 * How many different devices has this account installed on (in a certain period of time)?
3. How does location behave on devices?
 * Analyze the use of fake location and its activation

## Relevant Charts:

1. Mean value, maximum value, and standard deviation of age (bar chart)
2. Percentage of rooted devices (bar chart)
3. Logins by day of the week (pie chart)
4. Logins by timestamp (plot)
5. Emulator vs. Non-emulator (pie chart)
6. Devices per account in mode, mean, median, and standard deviation (bar chart)
7. Mean, median, and mode of restarts (bar chart)
8. Mean, median, and mode of daily restarts (bar chart)
9. Mean, median, and standard deviation of maximum apps installed per device
10. Percentage of apps installed outside of the official store (pie chart)

## Questions to Ask:

1. Is there a correlation between devices with more accounts per wallpaper and account takeover?
2. Emulators and Account Takeovers - Are they related?
3. Root vs. Non-root - Which is more related to account takeover?
4. Does the number of wallpapers have a correlation with account takeover?
5. How many devices have installations made outside of the official store? What is the average?
6. External Download (external_download) vs. Account Takeover Event - A heatmap
7. Suspicious Location vs. Account Takeover Event - A heatmap
8. Is there a correlation between the average number of boots per day and account takeover events?
9. Is there any day of the week where account takeovers occur more frequently?
10. Is there any correlation between each of the variables?
