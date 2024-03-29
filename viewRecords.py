def main(params):
	return{
	'statusCode':200,
	'headers':{'Content-Type':'text/html'},
	'body':'''
	<!DOCTYPE html>
<html>
<head>
	
	<meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Virus Detector</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap">
    <script src="https://code.jquery.com/jquery-3.4.1.js" integrity="sha256-WpOohJOqMqqyKL9FccASB9O0KwACQJpFTUBLTYOVvVU="crossorigin="anonymous"></script>
    <style type="text/css">
      .navbar{
        min-height: 76px !important;
      }
      .ml-auto{
        margin-right: 5vw;  
      }
      .nav-item,.nav-link{
        font-size: 1.5vw;
        font-family: Lato, sans-serif; 
          font-weight: bold;
        
      }
      .navbar-brand{
                border: 1px #ddd;
                border-radius: 4px;
                padding: 10px;
                width: 380px;
                align-self: center;
                /*margin: 2px*/
            }
            .rbh{
              height: 70px;
            }
            h2{
              font-size: 2.5vw;
              font-family: Lato, sans-serif; 
              font-weight: bold;

            }
            table.dataTable thead .sorting:after,
            table.dataTable thead .sorting:before,
            table.dataTable thead .sorting_asc:after,
            table.dataTable thead .sorting_asc:before,
            table.dataTable thead .sorting_asc_disabled:after,
            table.dataTable thead .sorting_asc_disabled:before,
            table.dataTable thead .sorting_desc:after,
            table.dataTable thead .sorting_desc:before,
            table.dataTable thead .sorting_desc_disabled:after,
            table.dataTable thead .sorting_desc_disabled:before {
              bottom: .5em;
            }
    </style>
</head>
<body onload="loadRecords()">
   <header class="sticky-top ">
        <nav class="navbar navbar-expand-lg navbar-dark " style="background-color: #bbdefb; color:#15386a; padding: 0px 15px 0px 15px;">
            <a href="#" class="navbar-brand">
                <!-- <img src="name.png" alt=""> -->
            </a>
            <button class="navbar-toggler btn-light float-right" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation" style="margin top:20px; margin-left:0px ">
                <span class="navbar-toggler-icon btn-light"></span>
            </button>
            <div class="collaspe navbar-collapse float-right" id="navbarNavAltMarkup">
                <div class="navbar-nav ml-auto" style="margin-left: 4vw;">
                <!-- <a class="nav-item nav-link" style="" href="#">Virus Detector</a> -->
                <a class="nav-item nav-link" style="color:#15386a; font-weight: bold;padding-right: 25px;padding-left: 25px;" href="https://eu-gb.functions.cloud.ibm.com/api/v1/web/vmk0888%40gmail.com_dev/default/submitImage2">Home</a>
                <a class="nav-item nav-link" style="color:#15386a; font-weight: bold;padding-right: 25px;padding-left: 25px " href="#">Records</a>
               <!-- <a class="nav-item nav-link" style="color:#15386a; font-weight: bold;" href="members.php">Membership</a> -->
                
                <a class="nav-item nav-link" style="color:#15386a; font-weight: bold;padding-right: 25px;padding-left: 25px;" href="https://eu-gb.functions.cloud.ibm.com/api/v1/web/vmk0888%40gmail.com_dev/default/loginPage2" onclick="preventBack()">Logout</a>
                </div>
            </div>
        </nav>
    </header>
  <div class="container-fluid" style="background-size: cover;background-color: #e3f2fd;padding: 0px; min-height: 90vh">
    <!-- <div style="background-color: #bbdefb; ">
      <h1 class="responsive text-sm-center" style="font-weight: bold; font-size: 9vh; font-family: Lato, sans-serif; color: #283593">
        Virus Detector
      </h1>
    </div> -->
    
    <div class="container" style="padding-top: 2vh; background-color: #e3f2fd;">
      <div class="row rbh">
        <div class="col-md-6 text-center offset-md-3">
        <center><h2  id="heading1">Patient Records</h2></center>
      </div>
    </div>
     <div class="row" style="padding-top: 20px">
      <div class="col-lg-12 col-md-12 col-sm-12">
        <div class="table-wrapper-scroll-y">
        <div id="dtBasicExample_wrapper" class="dataTables_wrapper dt-bootstrap4 no-footer">
          <div class="row">
            <div class="col-sm-12 col-md-6">
              <div class="dataTables_length bs-select" id="dtBasicExample_length">
                <label>Show entries
                  <select name="dtBasicExample_length" aria-controls="dtBasicExample" class="custom-select custom-select-sm form-control form-control-sm">
                    <option value="10">10</option>
                    <option value="25">25</option>
                    <option value="50">50</option>
                    <option value="100">100</option>
                  </select> 
                </label>
                </div>
              </div>
              <div class="col-sm-12 col-md-3 offset-md-3" style="padding-right: 0px ">
                <div id="dtBasicExample_filter" class="dataTables_filter" style="margin-right: 0px">
                  <label for="SearchButton" style="margin-left: 2vw;">Search:
                  <input id="SearchButton" name="SearchButton" type="text" class="form-control form-control-sm ml-auto float-right" placeholder="" aria-controls="dtBasicExample" style="margin-bottom: 2vh;">
                    <!-- <input type="search" name="searchbar" id="searchbar" onkeyup="" placeholder="Search"> -->
                 </label>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-lg-12">
                <table id="dtBasicExample" class="table table-striped table-bordered" cellspacing="0" width="100%">
                  <thead>
                    <tr>
                      <th class="th-sm">ImageID
                      </th>
                      <th class="th-sm">Name
                      </th>
                      <th class="th-sm">Gender
                      </th>
                      <th class="th-sm">Age
                      </th>
                      <th class="th-sm">date
                      </th>
                      <th class="th-sm">diagnosis
                      </th>
                      <th class="th-sm" colspan = 2>view Images
                      </th>
                      
                    </tr>
                  </thead>
                  <tbody id = 'tableBody'>
                    
    
                  </tbody>
              </table>
            </div>
          </div>  
        </div>
      </div>  
    </div>
  </div> 
</div>
<script type="text/javascript">
  getEntry = function(record){
    let entries = []
    for(let i = 0 ; i < 6 ; i++){
      entries.push(document.createElement('td'))
      console.log(i)
    }
    entries[0].appendChild(document.createTextNode(record['inf_image_id']))
    entries[1].appendChild(document.createTextNode(record['patient_name']))
    entries[2].appendChild(document.createTextNode(record['patient_gen']))
    entries[3].appendChild(document.createTextNode(record['patient_age']))
    entries[4].appendChild(document.createTextNode(record['patient_date']))
    entries[5].appendChild(document.createTextNode(record['inf_diagnosis']))
    console.log(entries)
    return entries;
  }
  let loadRecords = function(){
    let user_id = sessionStorage.getItem("user_id");
    xmlhttp = new XMLHttpRequest()
    xmlhttp.onreadystatechange = function(){

      if(this.readyState == 4 && this.status == 200){

        serverResponse = JSON.parse(this.responseText);
        records = serverResponse['data'];
        let table = document.querySelector('#dtBasicExample')
        for(let i = 0 ; i<records.length ; i++){

	        let row = table.insertRow(-1)
	        let cells = []
		        for(let j = 0 ; j <= 7 ; j++){
		        	cells.push(row.insertCell(j))
		        }
	        cells[0].innerHTML = records[i]['inf_image_id']
	        cells[1].innerHTML = records[i]['patient_name']
	        cells[2].innerHTML = records[i]['patient_gen']
	        cells[3].innerHTML = records[i]['patient_age']
	        cells[4].innerHTML = records[i]['patient_date']
	        cells[5].innerHTML = records[i]['inf_diagnosis']
          let cosImageId = records[i]['cos_image_id']

          let input_link = document.createElement("span");
          let output_link = document.createElement("span");

          input_link_id = "in/"+cosImageId
          output_link_id = "out/"+cosImageId

          input_link.id = input_link_id
          output_link.id = output_link_id
          input_text = document.createTextNode('view input');
          output_text = document.createTextNode('view output');

          input_link.style.margin = "0px 10px 10px 0px"
          output_link.style.margin = "0px 10px 10px 0px"
          input_link.style.cursor = "pointer"
          output_link.style.cursor = "pointer"

          input_link.style.color = "red"
          output_link.style.color = "red"

          input_link.appendChild(input_text);
          output_link.appendChild(output_text)
          input_link.addEventListener("click" , sendImageReq)
          output_link.addEventListener("click" , sendImageReq)




          //link.style.display = 'inline-block'
          
          cells[6].appendChild(input_link)
          cells[7].appendChild(output_link)

        }
        
      }

    }


    xmlhttp.open("POST" , "https://eu-gb.functions.cloud.ibm.com/api/v1/web/vmk0888%40gmail.com_dev/default/getRecords.json")
    xmlhttp.setRequestHeader("content-type","application/json")
    xmlhttp.send(JSON.stringify({'user_id':user_id , 'passwd':134}))
  }

  let sendImageReq = function(){
    console.log('sneding image req')
    let elementId = this.id
    let type = elementId.split('/')[0]
    let imageId =elementId.split('/')[1]
    console.log(imageId)
    xmlhttp = new XMLHttpRequest()
    xmlhttp.onreadystatechange=function(){
      if(this.status == 200 && this.readyState ==4){
        let response = JSON.parse(this.responseText)
        console.log(response)
        let imgString = "data:image/png;base64,"+response['body']
        let image = new Image()
        image.src = imgString;

        let w = window.open('about:blank');
        setTimeout(function(){
          
        w.document.write(image.outerHTML);
        }, 0);
      }
    }
    xmlhttp.open('POST','https://eu-gb.functions.cloud.ibm.com/api/v1/web/vmk0888%40gmail.com_dev/default/getCosImages.json')
    xmlhttp.setRequestHeader("content-type","application/json")
    xmlhttp.send(JSON.stringify({
      'item':imageId,
      'type':type
    }))


  }
 


</script>
<script type="text/javascript">
        function preventBack() { window.history.forward(); }
        setTimeout("preventBack()", 0);
        window.onunload = function () { null };
</script>
<script>
// $(document).ready(function () {
// $('#dtBasicExample').DataTable({
// "scrollX": "100%"
// });
// $('.dataTables_length').addClass('bs-select');
// });
$(document).ready(function(){

  // Search all columns
  $('#SearchButton').keyup(function(){
    // Search Text
    var search = $(this).val();

    // Hide all table tbody rows
    $('table tbody tr').hide();

    // Count total search result
    var len = $('table tbody tr:not(.notfound) td:contains("'+search+'")').length;

    if(len > 0){
      // Searching text in columns and show match row
      $('table tbody tr:not(.notfound) td:contains("'+search+'")').each(function(){
        $(this).closest('tr').show();
      });
    }else{
      $('.notfound').show();
    }

  });

  });

// Case-insensitive searching (Note - remove the below script for Case sensitive search )
$.expr[":"].contains = $.expr.createPseudo(function(arg) {
   return function( elem ) {
     return $(elem).text().toUpperCase().indexOf(arg.toUpperCase()) >= 0;
   };
});
</script>

</body>
</html>
	'''
	}