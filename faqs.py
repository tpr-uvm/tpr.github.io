main_page = """
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Twitch Plays Robotics</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <style>
    /* Set height of the grid so .sidenav can be 100% (adjust if needed) */
    .row.content {height: 1500px}
    
    /* Set gray background color and 100% height */
    .sidenav {
      background-color: #e2e2e2;
      height: 100%;
    }
    /* Set black background color, white text and some padding */
    footer {
      background-color: #555;
      color: white;
      padding: 15px;
      text-align: center;  
    }
    footer
    p
    a{
    text-decoration: underline;
    color: #96d4ec
    }
    /* On small screens, set height to 'auto' for sidenav and grid */
    @media screen and (max-width: 767px) {
      .sidenav {
        height: auto;
        padding: 15px;
      }
      .row.content {height: auto;} 
    }
   h2{
	text-align: center;
}
p{
margin-left: 7.5%;
margin-right: 7.5%;
line-height: 28px;
font-size: 16px;
}
li:hover
a:hover{
font-weight: bold;
background-color: #e2e2e2;
}
li
a{
-webkit-appearance: button;
    -moz-appearance: button;
    appearance: button;
    text-align: center;
    font-weight: bold;
    color: #111;
    }
  </style>
</head>
<body>
<div class="container-fluid">
  <div class="row content">
    <div class="col-sm-3 sidenav">
<img src="TPR.png" class="img-responsive" style="width: 90%; margin-right:auto; margin-left:auto; margin-top: 1em;" alt="TPR Logo">
      <h4>Menu</h4>
      <ul class="nav nav-pills nav-stacked">
        <li><a href="index.html">Home</a></li>
        <li><a href="users.html">Users</a></li>
        <li><a href="cmds.html">Commands</a></li>
        <li><a href="faqs.html">FAQs</a></li>
      </ul><br>  
    </div>
    <div class="col-sm-9">
      <hr>
      <h2>Twitch Plays Robotics</h2>
      <ul>
      	<li><a href="#project">Project</a></li>
      	<li><a href="#twitch">Twitch</a></li>
      	<li><a href="#robots">Robots</a></li>
      	<li><a href="#commands">Commands</a></li>
      	<li><a href="#reinforcements">Reinforcements</a></li>
      	<li><a href="#scores">Scores</a></li>
      	<li><a href="#relearning">Reinforcement Learning</a></li>
      </ul>
      
      <ul>
      	<li><div id="project">Project</div></li>
      	<li><div id="twitch">Twitch</div></li>
      	<li><div id="robots">Robots</div></li>
      	<li><div id="commands">Commands</div></li>
      	<li><div id="reinforcements">Reinforcements</div></li>
      	<li><div id="scores">Scores</div></li>
      	<li><div id="relearning">Reinforcement Learning</div></li>
      </ul>
    </div>
  </div>
</div>
<footer class="container-fluid">
  <p><a href="https://www.meclab.org">Morphology, Evolution, Cognition Lab</a></p>
</footer>
</body>
</html>
"""
f = open('faqs.html','w')
f.write(main_page)
f.close()


