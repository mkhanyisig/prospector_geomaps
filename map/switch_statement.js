switch(country){
    case "Mexico":
        var res = httpGet(country_mapobj[country]);

        var obj = JSON.parse(res);

        // update map properties
        // center
        geocoder.geocode( {'address' : country}, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                map.setCenter(results[0].geometry.location);
            }
        });

        // set zoom
        map.setZoom(5);
        var zoom = document.getElementById("zoom");
        zoom.options[zoom.selectedIndex].value=5;
        console.log(country+" zoom: "+map.zoom);

        // update points
        eqfeed_callback(obj);

        break;
    case "Canada":
        var res = httpGet(country_mapobj[country]);

        var obj = JSON.parse(res);

        // update map properties
        // center
        geocoder.geocode( {'address' : country}, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                map.setCenter(results[0].geometry.location);
            }
        });

        // set zoom
        map.setZoom(4);
        var zoom = document.getElementById("zoom");
        zoom.options[zoom.selectedIndex].value=4;
        console.log(country+" zoom: "+map.zoom);

        // update points
        eqfeed_callback(obj);

        break;
    case "Guatemala":
        var res = httpGet(country_mapobj[country]);

        var obj = JSON.parse(res);

        // update map properties
        // center
        geocoder.geocode( {'address' : country}, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                map.setCenter(results[0].geometry.location);
            }
        });

        // set zoom
        map.setZoom(8);
        var zoom = document.getElementById("zoom");
        zoom.options[zoom.selectedIndex].value=8;
        console.log(country+" zoom: "+map.zoom);

        // update points
        eqfeed_callback(obj);

        break;
    case 'Croatia':

        var res = httpGet(country_mapobj[country]);

        var obj = JSON.parse(res);

        // update map properties
        // center
        geocoder.geocode( {'address' : country}, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                map.setCenter(results[0].geometry.location);
            }
        });

        // set zoom
        map.setZoom(7);
        var zoom = document.getElementById("zoom");
        zoom.options[zoom.selectedIndex].value=7;
        console.log(country+" zoom: "+map.zoom);

        // update points
        eqfeed_callback(obj);

        break;
    case 'Czech Republic':
        var res = httpGet(country_mapobj[country]);

        var obj = JSON.parse(res);

        // update map properties
        // center
        geocoder.geocode( {'address' : country}, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                map.setCenter(results[0].geometry.location);
            }
        });

        // set zoom
        map.setZoom(7);
        var zoom = document.getElementById("zoom");
        zoom.options[zoom.selectedIndex].value=7;
        console.log(country+" zoom: "+map.zoom);

        // update points
        eqfeed_callback(obj);

        break;
    case 'Russian Federation':
        var res = httpGet(country_mapobj[country]);

        var obj = JSON.parse(res);

        // update map properties
        // center
        geocoder.geocode( {'address' : country}, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                map.setCenter(results[0].geometry.location);
            }
        });

        // set zoom
        map.setZoom(3);
        var zoom = document.getElementById("zoom");
        zoom.options[zoom.selectedIndex].value=3;
        console.log(country+" zoom: "+map.zoom);

        // update points
        eqfeed_callback(obj);

        break;
    case 'Hungary':
        var res = httpGet(country_mapobj[country]);

        var obj = JSON.parse(res);

        // update map properties
        // center
        geocoder.geocode( {'address' : country}, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                map.setCenter(results[0].geometry.location);
            }
        });

        // set zoom
        map.setZoom(7);
        var zoom = document.getElementById("zoom");
        zoom.options[zoom.selectedIndex].value=7;
        console.log(country+" zoom: "+map.zoom);

        // update points
        eqfeed_callback(obj);

        break;
    case 'Iraq':
        var res = httpGet(country_mapobj[country]);

        var obj = JSON.parse(res);

        // update map properties
        // center
        geocoder.geocode( {'address' : country}, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                map.setCenter(results[0].geometry.location);
            }
        });

        // set zoom
        map.setZoom(7);
        var zoom = document.getElementById("zoom");
        zoom.options[zoom.selectedIndex].value=7;
        console.log(country+" zoom: "+map.zoom);

        // update points
        eqfeed_callback(obj);

        break;
    case 'Mauritania':
        var res = httpGet(country_mapobj[country]);

        var obj = JSON.parse(res);

        // update map properties
        // center
        geocoder.geocode( {'address' : country}, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                map.setCenter(results[0].geometry.location);
            }
        });

        // set zoom
        map.setZoom(5);
        var zoom = document.getElementById("zoom");
        zoom.options[zoom.selectedIndex].value=5;
        console.log(country+" zoom: "+map.zoom);

        // update points
        eqfeed_callback(obj);

        break;
    case 'Philippines':
        var res = httpGet(country_mapobj[country]);

        var obj = JSON.parse(res);

        // update map properties
        // center
        geocoder.geocode( {'address' : country}, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                map.setCenter(results[0].geometry.location);
            }
        });

        // set zoom
        map.setZoom(7);
        var zoom = document.getElementById("zoom");
        zoom.options[zoom.selectedIndex].value=7;
        console.log(country+" zoom: "+map.zoom);

        // update points
        eqfeed_callback(obj);

        break;
    case 'Congo (Kinshasa)':
        var res = httpGet(country_mapobj[country]);

        var obj = JSON.parse(res);

        // update map properties
        // center
        geocoder.geocode( {'address' : country}, function(results, status) {
            if (status == google.maps.GeocoderStatus.OK) {
                map.setCenter(results[0].geometry.location);
            }
        });

        // set zoom
        map.setZoom(7);
        var zoom = document.getElementById("zoom");
        zoom.options[zoom.selectedIndex].value=7;
        console.log(country+" zoom: "+map.zoom);

        // update points
        eqfeed_callback(obj);

        break;
    default:
        console.log("Default: no country selected");

  }
