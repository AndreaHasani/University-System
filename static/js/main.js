$(document).ready(function(){
  $("#table-search").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $(".adm-table tbody tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
  });
});


// Add option / $("#subjects").append(new Option("option text", "value"));
$( "#remove-button" ).click(function() {
    $('#subjects').append($('#subjects_failed').find('option:selected'));
    $('#subjects_failed').find('option:selected').remove().end();
});


$( "#add-button" ).click(function() {
    $('#subjects_failed').append($('#subjects').find('option:selected'));
    $('#subjects').find('option:selected').remove().end();
});


// Submit Jquery



$( ".submit-button input" ).click(function() {
    var firstInfo= [];
    $(".first-info input").each(function (index) {
	firstInfo.push($(this ).val());
    });
    var subjects = [];
    $("#subjects option").each(function (index) {
	subjects.push($(this ).val());
    });

    var subjectsFailed = [];
    $("#subjects_failed option").each(function (index) {
	subjectsFailed.push($(this ).val());
    });

    var id = document.location.href.substr(document.location.href.lastIndexOf('/') + 1);
    console.log(id);

    $.ajax({
	type: "POST",
	url: "http://0.0.0:5005/rest/adm_edit",
	data: {
	    'first': firstInfo.join(), 
	    'second': subjects.join(), 
	    'third': subjectsFailed.join(),
	    'id': id,
	},
	dataType: "json",
	success: function(data) {
	    console.log(data.result + ' ' + data.code);
	    $( ".submit-button input" ).css("background-color", "green");
	},
	error: function(data) {
	    console.log(data.result + ' ' + data.code);
	    $( ".submit-button input" ).css("background-color", "red");
	}

    });
});

