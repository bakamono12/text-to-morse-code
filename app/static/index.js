$(document).ready(function() {
    $("#convert-button").click(function() {
        const userInput = $("#input-text").val().trim().toUpperCase();
        const morseOutput = $("#morse-output");

        if (userInput === "") {
            morseOutput.val("Please enter text.");
            return;
        }

        $.ajax({
            url: `/convert?text=${encodeURIComponent(userInput)}`,
            method: "GET",
            success: function(data) {
                morseOutput.val(data);
            },
            error: function(xhr, status, error) {
                console.error("An error occurred:", error);
                morseOutput.val("An error occurred.");
            }
        });
    });
});
