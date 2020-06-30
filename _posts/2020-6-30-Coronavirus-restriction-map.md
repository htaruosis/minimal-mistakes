---
layout: single
title: "Map of postcodes with Stage Three restrictions"
categories: [maps]
tags: 
search: true
excerpt: 
excerpt_separator: <!--more-->
published: true
header:
  og_image: 
---
    
<style>
    .mapid { 
      position: relative;
      padding-bottom: 75%; // This is the aspect ratio
      height: 0;
      overflow: hidden;
    }
</style>
    
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css" integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ==" crossorigin=""/>

<script src="https://unpkg.com/leaflet@1.6.0/dist/leaflet.js" integrity="sha512-gZwIG9x3wUXg2hdXF6+rVkLF/0Vi9U8D2Ntg4Ga5I5BZpVkVxlJWbSQtXPSiUTtC0TjtGOmxa1AJPuV0CPthew==" crossorigin=""></script>
   
<script src="/images/2020-06/user_polygon/VMADMIN/leaflet_ajax.js"></script>
   
<div class="mapid" id ="mapid"></div>

<script>
    function style(feature) {
        if (feature.properties.Stage3 == 'Yes') {
            return {
                fillColor: 'red',
                color: 'red',
                weight: 1,
                opacity: 1,
                fillOpacity: 0.2
                };
            }
        else {
                return {
            fillColor: 'green',
            color: 'green',
            weight: 1,
            opacity: 1,
            fillOpacity: 0.1
            };
        }
    }
    function zoomToFeature(e) {
        mymap.fitBounds(e.target.getBounds());
    }

    function onEachFeature(feature, layer) {
		layer.bindPopup("<p>Postcode: " + feature.properties.POSTCODE + "<br>Stage three restrictions: " + feature.properties.Stage3 + "</p>");
        layer.on({
            click: zoomToFeature
        });
    }
    var mymap = L.map('mapid').setView([-37.8174, 144.9564], 11);
    L.tileLayer('https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png', {
        maxZoom: 20, 
        attribution: '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors | Postcodes from <a href="https://discover.data.vic.gov.au/dataset/postcode-boundaries-polygon-vicmap-admin">DELWP</a> under CC BY 4.0'
    }).addTo(mymap); 
    var geojsonLayer = new L.GeoJSON.AJAX("/images/2020-06/user_polygon/VMADMIN/postcode_1.json" ,{style: style, onEachFeature: onEachFeature});
    geojsonLayer.addTo(mymap);
    // add GeoJSON layer to the map once the file is loaded
//    var datalayer = L.geoJson(geojsonLayer ,{
//    onEachFeature: function(feature, featureLayer) {
//    featureLayer.bindPopup(feature.properties.POSTCODE);
//    }
//    }).addTo(mymap);
//    mymap.fitBounds(datalayer.getBounds());
//    });
</script>