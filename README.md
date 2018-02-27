<img src="http://www.alumnux.com/assets/images/icon/Data-Visualization.png" align="right" width="150px" />

# Data Visualisation Projects

> This repository contains a collection of data-visualisation projects undertaken for the primary purpose of learning new skills, practicing data manipulation & visualisation and producing beautiful insights from data.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## Table of Contents

1. [2017 Hourly Weather in New Delhi, India](#1-2017-hourly-weather-in-new-delhi-india)
  - [Description](#description)
    - <a href="https://codepen.io/utkarshmttl/full/PQyWvG/" target="_blank">Codepen</a>

    - [Live Demo](https://utkarshmttl.github.io/data-visualisation/weather/) (for interactive tooltips)
  - [How I made this?](#how-i-made-this-)
  - [New Skills Acquired](#new-skills-acquired)
  - [Old Skills Practiced](#old-skills-practiced)
  - [Analysis](#analysis)
  - [Questions?](#questions-)

2. [Coming Soon...](#2-coming-soon-)

3. [Authors](#authors)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


## 1. 2017 Hourly Weather in New Delhi, India

<a href="https://utkarshmttl.github.io/data-visualisation/weather/"><img src="./weather/screenshots/2.png"></a>

<a name="description"></a>

The above visualisation represents the hourly 2017 temperature in New Delhi, India. Each revolution (ring) represents a single day, innermost being January 1st 2017 and outer most being December 31st 2017. Midnight is at top (24 hour clock), so the right half represents midnight to noon and the left half noon to midnight.

* [Codepen](https://codepen.io/utkarshmttl/full/PQyWvG/)

* [Live Demo](https://utkarshmttl.github.io/data-visualisation/weather/) (for interactive tooltips)

This project was INSPIRED from [one of the top posts](https://www.reddit.com/r/dataisbeautiful/comments/5l39mu/my_daughters_sleeping_patterns_for_the_first_4/) on [r/dataisbeautiful](https://www.reddit.com/r/dataisbeautiful) of all time.

#### How I made this?
<!-- ___ -->
The data was obtained from WeatherUnderground using [`data_wunderground.py`](./weather/data_wunderground.py).

A big vote of thanks to [Weather Underground](https://www.wunderground.com/) for functioning as a very good data source for historical temperature data.

Things that needed to be taken care of:
- Extraneous values - the data for some days had temperature data at times like 12:01, 12:03 extra which was not if use to use since we considered data at times starting from 00:00 to 23:30 each day at half hour intervals.

- Missing values - the data for some days did not have temperature data for required times. The missing values were interpolated using `pandas.DataFrame.interpolate(method="cubic")` function.

- Repeat values - sometimes there were 2 values for same time and also sometimes a heading of time was there with null temperature value. These edge cases also had to be considered.

After the final data was obtained, d3.js arc function was used to create 48 arcs for each day, each arc representing temperature of the corresponding half hour period. The start & end angles and inner & outer radii for each arc were calculated mathematically. The inner and outer radii were same for arcs corresponding to the same day and increased as we moved outwards.

The function
```javascript
function getColor(value){
    //value from 0 to 1
    var hue=((1-value)*240).toString(10);
    return ["hsl(",hue,",100%,50%)"].join("");
}
```
returns a color based on percentage (0 to 1) along a gradient from blue (representing cold) to red (representing hot).

The color of each arc was set using this function, passing the temperature (as a percentage between min = 4°C and maximum = 48.3°C) as an input to the `getColor` function.

Tooltips were added to display the date, time and temperature values on mouse hover event.

#### New Skills Acquired

- [d3.js](https://d3js.org/) - Has a steeper learning curve than I had expected. It was challenging yet fun to explore this very popular data visualisation JavaScript library.
- Data visualisation concepts.


#### Old Skills Practiced

- Python/automation scripting
- Data mining and preprocessing
- Data manipulation

#### Analysis

- The innermost and outermost regions are the coldest. Expected. Since January and December are the coldest months in New Delhi. Even with these regions, mostly night time is colder.
- The region of second quarter of the year is hottest. Again, expected. Even with these regions, mostly day time is hotter.
- Considerable portion is green which means the temperature is average-ish for most time.
- The number of days when it was hot for most part of the day is lesser than the number of days when it was cold for most part of the day.
- Two suddenly cold temperatures (at around 4 PM) during hot season might be either outliers or error in recording in the source website.


- Shortcomings
  - The circumference gets larger as we move towards end of year, which enlarges the cell area on the heatmap, making it perceptually seem like hotter/colder temperatures persist for a longer time. There are a couple possibilities. First to enlarge the center radius so the difference is minuscule. Another possibility is to plot the heatmap onto rectilinear coordinates, x=days, y=time of day (or vice-versa), [similar to this](http://i.imgur.com/8YZ6VsZ.png). I will try to make a rectangular version soon.
  - But it looks so good!


- Future works
  - Comparing 2007 (or older) vs 2017 charts with transitioning animations to see how temperature patterns have changed over time.
  - Comparing charts for different geographical locations.

#### Questions?

Want to make a similar visualisation and having trouble getting started? or have some queries in general? Raise an issue or contact me at the given email address.

## 2. Coming Soon...

<br><br>

##  

<a href="http://ducic.ac.in/"><img src="https://user-images.githubusercontent.com/16596327/30467922-9d4985ce-9a05-11e7-81aa-9f5348eb40de.png" align="right" width="300"/></a>
## Author



* **[Utkarsh Mittal](https://github.com/utkarshmttl)** - *utkarshmttl@gmail.com*
