// Call the dataTables jQuery plugin
//$(document).ready(function() {
//  $('#dataTable').DataTable();
//});

$.getJSON("http://journal.kami-nashi.com/skatetrax.core/sessions-brief_json.php", function(jsonFromFile) {
  $('#dataTable').bootstrapTable({
    data: jsonFromFile,
    "pagingType": "full_numbers"
  });
   $('.dataTables_length').addClass('bs-select');
});

