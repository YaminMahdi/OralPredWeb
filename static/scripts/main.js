console.log("script init");
const asyncGetPrediction = async () => {
    try {
        const response = await fetch("/prediction");
            const data = await response.json();
            console.log(data);
            $(".loading").hide();
            const cls = data["class"];
            if(cls === "Normal")
                $('.predTxt').css('color', '#4beb4b');
            else
                $('.predTxt').css('color', '#ff7373');
            $(".predTxt").text(cls);
            $(".predPer").text("Accuracy: " + data["accuracy"]);
            $(".pred").show();
            $(".getPrediction").show();

        } catch(error) {
            $(".loading").hide();
            $('.predTxt').css('color', '#ff7373');
            $(".predTxt").text(error);
            $(".predPer").text("");
            $(".pred").show();
            $(".getPrediction").show();
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