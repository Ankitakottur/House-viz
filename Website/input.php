
<html>
<head>
  <title>House.Viz</title>
  <meta charset="utf-8">
  <link type="text/css" href="input.css" rel="stylesheet">
</head>

<body>

  <div class="main">

    <div class="form">

      <form method="POST" action="heatmap.html" id="contact-form" class="form">

          <div class="form-group">

            <select name="Budget" class="dropdown" value="Select a budget">
              <option value="range1">$50,000 - $100,000</option>
              <option value="range2">$100,000 - $200,000</option>
              <option value="range3">$200,000 - $300,000</option>
              <option value="range4">$300,000 - $400,000</option>
              <option value="range4">$400,000 - $500,000</option>
              <option value="range4">$500,000 - $600,000</option>
              <option value="range4">$600,000 - $700,000</option>
              <option value="range4">$700,000 - $800,000</option>
              <option value="range4">$800,000 - $900,000</option>
              <option value="range4">$900,000 - $1,000,000</option>
              <option value="range4">$1,000,000 - $1,500,000</option>
              <option value="range4">$1,500,000 - $5,000,000</option>
              <option value="range4">$5,000,000 - $7,750,000</option>
            </select>  
            <br><br>
            <select name="Area" class="dropdown">
              <option value="area1">300 - 1000 sq.ft</option>
              <option value="area2">1000 - 1500 sq.ft</option>
              <option value="area3">1500 - 2000 sq.ft</option>
              <option value="area4">2000 - 2500 sq.ft</option>
              <option value="area4">2500 - 3000 sq.ft</option>
              <option value="area4">3000 - 4000 sq.ft</option>
              <option value="area4">4000 - 5000 sq.ft</option>
              <option value="area4">5000 - 6000 sq.ft</option>
              <option value="area4">6000 - 7000 sq.ft</option>
              <option value="area4">7000+ sq.ft</option>
            </select>
            <br><br>  
            <select name="Radius" class="dropdown">
              <option value="range1">500m</option>
              <option value="range2">1000m</option>
            </select>
            <br><br><br>
            <button type="submit" class="btn btn-success" value="login">Search</button>
          </div>

      </form>
    </div>
  </div>


  <!-- Bootstrap core JavaScript -->
      <!-- Placed at the end of the document so the pages load faster -->
    <script src="js/jquery.js"></script>
    <script src="js/jquery-scrolltofixed-min.js"></script>
    <script src="js/jquery.vegas.js"></script>
    <script src="js/jquery.mixitup.min.js"></script>
    <script src="js/jquery.validate.min.js"></script>
    <script src="js/script.js"></script>
    <script src="js/bootstrap.js"></script>

  <!-- Slideshow Background  -->
    <script>
  $.vegas('slideshow', {
    delay:3000,
    backgrounds:[
       { src:'./images/h1.jpg', fade:1500 },
     { src:'./images/h2.jpg', fade:1500 },
      { src:'./images/h3.jpg', fade:1500 },
     { src:'./images/h4.jpg', fade:1500 },
      { src:'./images/h5.jpg', fade:1500 },
      { src:'./images/h6.jpg', fade:1500 },
    ]
  });
  ('overlay', {
  src:'./img/overlay.png'
  });
    </script>
  <!-- /Slideshow Background -->

  <!-- Mixitup : Grid -->
      <script>
      $(function(){
      $('#Grid').mixitup();
        });
      </script>
  <!-- /Mixitup : Grid -->

      <!-- Custom JavaScript for Smooth Scrolling - Put in a custom JavaScript file to clean this up -->
      <script>
        $(function() {
          $('a[href*=#]:not([href=#])').click(function() {
            if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'')
              || location.hostname == this.hostname) {

              var target = $(this.hash);
              target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
              if (target.length) {
                $('html,body').animate({
                  scrollTop: target.offset().top
                }, 1000);
                return false;
              }
            }
          });
        });
      </script>


</body>

</html>
