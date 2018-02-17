function selectSample() {
    var route = "/names";

    d3.json(route, function(error, response) {
        var data = response;

        var dropdown = d3.select("#dropdown");
        dropdown
            .append("select")
            .attr("id", "selDataset")
            .on("change", optionChanged(this.value))
            .selectAll("option")
            .data(data)
            .enter()
            .append("option")
            .attr("value", d => d)
            .text(d => d);
    });
}

function metadataPanel(sample) {
    var route = "/metadata/"+ sample;

    d3.json(route, function(error, response) {
        var data = response;
        var panel = d3.select("#infopanel");

        panel.append("p").text("AGE: " + data.AGE);
        panel.append("p").text("BBTYPE: " + data.BBTYPE);
        panel.append("p").text("ETHNICITY: " + data.ETHNICITY);
        panel.append("p").text("GENDER: " + data.GENDER);
        panel.append("p").text("LOCATION: " + data.LOCATION);
        panel.append("p").text("SAMPLEID: " + data.SAMPLEID);
    });
}

function optionChanged(sample) {
    
}

selectSample();
metadataPanel("BB_940");