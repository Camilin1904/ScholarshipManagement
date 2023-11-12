function idSearch() {
    // Declare variables
    var input, filter, table, tr, th, i, txtValue;
    // search field
    input = document.getElementById('id');
    // get the text on the search field
    filter = input.value.toUpperCase();
    // get table
    table = document.getElementById("schTable");
    // get all rows inside the table
    tr = table.getElementsByTagName('tr');
    // Loop through all list items, and hide those who don't match the search query
    for (i = 1; i < tr.length; i++) {
      // get the firts th from the ith tr
      td = tr[i].getElementsByTagName("td")[1];
      // extract the text inside th
      txtValue = td.textContent || td.innerText;
      // does the th element contains the filter?
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
          // if the index bigger that -1 the th element contains the filter
          tr[i].style.display = "";
      } else {
          // if the index is -1 the th element does not contains the filter
          tr[i].style.display = "none";
      }
    }
  }
  function nameSearch() {
    // Declare variables
    var input, filter, table, tr, th, i, txtValue;
    // search field
    input = document.getElementById('name');
    // get the text on the search field
    filter = input.value.toUpperCase();
    // get table
    table = document.getElementById("schTable");
    // get all rows inside the table
    tr = table.getElementsByTagName('tr');
    // Loop through all list items, and hide those who don't match the search query
    for (i = 1; i < tr.length; i++) {
      // get the firts th from the ith tr
      td = tr[i].getElementsByTagName("td")[0];
      // extract the text inside th
      txtValue = td.textContent || td.innerText;
      // does the th element contains the filter?
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
          // if the index bigger that -1 the th element contains the filter
          tr[i].style.display = "";
      } else {
          // if the index is -1 the th element does not contains the filter
          tr[i].style.display = "none";
      }
    }
  }
  function donorSearch() {
    // Declare variables
    var input, filter, table, tr, th, i, txtValue;
    // search field
    input = document.getElementById('donor');
    // get the text on the search field
    filter = input.value.toUpperCase();
    // get table
    table = document.getElementById("schTable");
    // get all rows inside the table
    tr = table.getElementsByTagName('tr');
    // Loop through all list items, and hide those who don't match the search query
    for (i = 1; i < tr.length; i++) {
      // get the firts th from the ith tr
      td = tr[i].getElementsByTagName("td")[2];
      // extract the text inside th
      txtValue = td.textContent || td.innerText;
      // does the th element contains the filter?
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
          // if the index bigger that -1 the th element contains the filter
          tr[i].style.display = "";
      } else {
          // if the index is -1 the th element does not contains the filter
          tr[i].style.display = "none";
      }
    }
  }