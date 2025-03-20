/*Скрипт JS: Обработка действия нажатия кнопки "Send"*/
$(document).ready(function(){  
    $('#sendBnt').click(function(e){
        console.log("!!")
        e.preventDefault();
        var prompt = $("#prompt").val().trimEnd();
        console.log(prompt);
        if(prompt == ""){
            $("#response").html("<small class='text-secondary'>Please ask a question. </small>");
        }
        else{            
            $("#response").html("<small class='text-secondary'>Waiting for response ... </small>");        
            $.ajax({
                url: "/query",
                method:"POST",
                data: JSON.stringify({input: prompt}),
                contentType:"application/json; charset=utf-8",
                dataType:"json",
                success: function(data){
                    $("#content").append("<div class='chat-message-right mb-4'><div class='flex-shrink-1 bg-success bg-opacity-10 rounded py-2 px-3 ml-3' id='query'><p><b>You:</b></p><div class='text-break'>" + data.query  + "</div></div></div>");                  
                    $("#content").append("<div class='chat-message-left pb-4'><div class='flex-shrink-1 bg-light rounded py-2 px-3 ml-3' id='answers'><p><b>QA-bot:</b></p><div class='text-break'>" + data.response + "</div></div></div>");                     
                    $("#response").html("<small class='text-secondary'></small>");
                    $("#prompt").val("");
                }
              })   
              
        }
    });     
}); 