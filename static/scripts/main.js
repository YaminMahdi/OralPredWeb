console.log("script init");
const asyncGetPrediction = async () => {
    try {
        const response = await fetch("/prediction");
            const data = await response.json();
            console.log(data);
            $(".loading").hide();
            $(".predTxt").text(data["class"]);
            $(".predPer").text("Accuracy: " + data["accuracy"]);
            $(".pred").show();
            $(".getPrediction").show();

        } catch(error) {
            console.log(error)
        } 
    }
$(document).ready(function() {
    $(".getPrediction").click(function() {
        console.log("btn click");
        $(".loading").show();
        $(".getPrediction").hide();
      asyncGetPrediction()        
    });
});