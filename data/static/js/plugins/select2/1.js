<html>
<head>
<script type="text/javascript" src="/jquery/jquery.js"></script>
<script type="text/javascript">
$(document).ready(function(){
  $("#b01").click(function(){
  htmlobj=$.ajax({url:"/api/users/v1/users/",async:false});
  $("#myDiv").html(htmlobj.responseText);
  });
});
</script>
</head>
<body>

<div id="myDiv"><h2>通过 AJAX 改变文本</h2></div>
<button id="b01" type="button">改变内容</button>

</body>
</html>
