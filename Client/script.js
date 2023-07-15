function getRoomsValue() {
    var uiRooms = document.getElementsByName("uiRooms");
    for (var i in uiRooms) {
        if (uiRooms[i].checked) {
            return parseInt(uiRooms[i].value);
        }
    }
    return -1; // Invalid Value
}

function getBathroomsValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for (var i in uiBathrooms) {
        if (uiBathrooms[i].checked) {
            return parseInt(uiBathrooms[i].value);
        }
    }
    return -1; // Invalid Value
}

function getCarSpacesValue() {
    var uiCar = document.getElementsByName("uiCar");
    for (var i in uiCar) {
        if (uiCar[i].checked) {
            return parseInt(uiCar[i].value);
        }
    }
    return -1; // Invalid Value
}

function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var distance = document.getElementById("uiDistance");
    var landsize = document.getElementById("uiLandsize");
    var rooms = getRoomsValue();
    var bathrooms = getBathroomsValue();
    var carSpaces = getCarSpacesValue();
    var suburb = document.getElementById("uiSuburbs");
    var property_type = document.getElementById("uiType");
    var region_name = document.getElementById("uiRegion");
    var estimatedPrice = document.getElementById("uiPredictPrice");

    var url = "http://127.0.0.1:5000/predict_price";

    $.post(url, {
        rooms: rooms,
        distance: parseFloat(distance.value),
        bathroom: bathrooms,
        car: carSpaces,
        landsize: parseFloat(landsize.value),
        suburb: suburb.value,
        property_type: property_type.value,
        region_name: region_name.value
    }, function (data, status) {
        console.log(data.estimated_price);
        estimatedPrice.innerHTML = "<h2>$" + data.estimated_price.toString() + "</h2>";
        console.log(status);
    });
}
/*
function onPageLoad() {
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_unique_values";
  
    $.get(url, function (data, status) {
      console.log("got response for get_unique_values request");
      if (data) {
        var suburbs = data.suburbs;
        var propertyTypes = data.property_types;
        var regionNames = data.region_names;
        var uiSuburbs = document.getElementById("uiSuburbs");
        var uiTypes = document.getElementById("uiType");
        var uiRegions = document.getElementById("uiRegion");
  
        $('#uiSuburbs').empty();
        for (var i in suburbs) {
          var opt = new Option(suburbs[i]);
          $('#uiSuburbs').append(opt);
        }
  
        $('#uiType').empty();
        for (var i in propertyTypes) {
          var opt = new Option(propertyTypes[i]);
          $('#uiType').append(opt);
        }
  
        $('#uiRegion').empty();
        for (var i in regionNames) {
          var opt = new Option(regionNames[i]);
          $('#uiRegion').append(opt);
        }
      }
    });
  }
*/

function onPageLoad() {
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_unique_values";

    $.get(url, function (data, status) {
        console.log("got response for get_unique_values request");
        console.log("Data:", data); // Add this line
        console.log("Status:", status); // Add this line
        if (data) {
            var suburbs = data.suburbs;
            var propertyTypes = data.property_types;
            var regionNames = data.region_names;
            var uiSuburbs = document.getElementById("uiSuburbs");
            var uiTypes = document.getElementById("uiType");
            var uiRegions = document.getElementById("uiRegion");

            $('#uiSuburbs').empty();
            for (var i in suburbs) {
                var opt = new Option(suburbs[i]);
                $('#uiSuburbs').append(opt);
            }

            $('#uiType').empty();
            for (var i in propertyTypes) {
                var opt = new Option(propertyTypes[i]);
                $('#uiType').append(opt);
            }

            $('#uiRegion').empty();
            for (var i in regionNames) {
                var opt = new Option(regionNames[i]);
                $('#uiRegion').append(opt);
            }
        }
    });
}

window.onload = onPageLoad;