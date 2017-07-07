console.log("Test JS");



//voivodeship , id's,
$(document).ready(function(){

    window.onload = getRegion;
    function getRegion(){
        $.ajax({
            url: "/region/api/",
            type: "GET"
        })
        .done((response, state) => {
            let selectRegion = $('#id_region');
            selectRegion.html('');
            let selectCity = $('#id_city');
            selectCity.html('');
            // selectCities.prop("hidden", "true")
            selectRegion.append("<option selected disabled hidden>Wybierz województwo</option>");
            $(response).each((i, region) => {
                console.log(region);
                selectRegions.append("<option value='"+region.id+"'>"+region.name+"</option>");
            })
            selectRegion.change();
            selectRegion.change(getCity);
        })
    };

    function getCity(){
        $('#id_city').removeAttr("hidden");
        let region = $('#id_region').val();
        $.ajax({
            url: "/region/api/"+region+"/city/",
            type: "GET"
        })
        .done((response, state) => {
            let selectCity = $('#id_city');
            selectCity.html('');
            $(response).each((i, city) => {
                console.log(city);
                selectCity.append("<option value='"+city.id+"'>"+city.name+"</option>");
            })
        })
    };
});
