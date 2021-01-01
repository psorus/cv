h1="""<style>dl {
    padding: 0.5em;
  }
  dt {
    float: left;
    clear: left;
    width: 100px;
    text-align: right;
    font-weight: bold;
    color: #333;
  }
  dt::after {
    content: ":";
  }
  dd {
    margin: 0 0 0 110px;
    padding: 0 0 0.5em 0;
  }</style>"""
h1="""<style type="text/css">

  dl {
    display: flex;
    flex-flow: row wrap;
    border: solid #333;
    border-width: 1px 1px 0 0;
  }
  dt {
    flex-basis: 20%;
    padding: 2px 4px;
    background: #111;
    text-align: right;
    color: #fff;
    font-size: ##fs##;

  }
  dd {
    flex-basis: 70%;
    flex-grow: 1;
    margin: 0;
    padding: 2px 4px;
    border-bottom: 1px solid #333;
    font-size: ##fs##;

  }

</style>"""
h2="""<style>
* {
  box-sizing: border-box;
}

.column {
  float: left;
  width: 50%;
  padding: 10px;
}

.row:after {
  content: "";
  display: table;
  clear: both;
}
</style>"""
h3="""<style>.square{
    counter-reset: list-counter;
    list-style: none;
    float:left;
}

.square li:before{
    content: counter(list-counter);
    counter-increment: list-counter;
    width: 1em;
    height: 1em;
    padding: .25em;
    margin-right: 1em;
    background: #111;
    color: #fff;
    font-family: arial;
    text-align: center;
    display: inline-block;
    
}</style>"""


h4="""<style>ul.timeline1 li
{
  position: relative;
  height: 3em;
  color: #333;
}

ul.timeline1 li:before
{
    content: "";
    display: inline-block;
    width: 1px;
    background: [backcolor];
    margin: 0;
    padding: 0;
    position: absolute;
    left: -11px;
    top: -0.4em;
    z-index: -1;
}

ul.timeline1:before
{
  content: "●";
  display: inline-block;
  margin: 0;
  padding: 0;
  position: relative;
  left: -1em;
  top: 0.1em;
  color: #aaa;
}

ul.timeline1:after
{
  content: "●";
  display: inline-block;
  margin: 0;
  padding: 0;
  position: relative;
  left: -1em;
  top: -1em;
  color: #aaa;
}</style>"""

h5="""<style>* {
  box-sizing: border-box;
}

/* Set a background color */
body {
  background-color: [backcolor];
  font-family: Helvetica, sans-serif;
}

/* The actual timeline (the vertical ruler) */
.timeline {
  position: relative;
  max-width: 1200px;
  margin: 0 auto;
}

/* The actual timeline (the vertical ruler) */
.timeline::after {
  content: '';
  position: absolute;
  width: 6px;
  background-color: [backcolor];
  top: 0;
  bottom: 0;
  left: 50%;
  margin-left: -3px;
}

/* Container around content */
.container {
  padding: 10px 40px;
  position: relative;
  background-color: [backcolor];
  width: 50%;
}

/* The circles on the timeline */
.container::after {
  content: '';
  position: absolute;
  width: 25px;
  height: 25px;
  right: -17px;
  background-color: [backcolor];
  border: 4px solid #FF9F55;
  top: 15px;
  border-radius: 50%;
  z-index: 1;
}

/* Place the container to the left */
.left {
  left: 0;
}

/* Place the container to the right */
.right {
  left: 50%;
}

/* Add arrows to the left container (pointing right) */
.left::before {
  content: " ";
  height: 0;
  position: absolute;
  top: 22px;
  width: 0;
  z-index: 1;
  right: 30px;
  border: medium solid white;
  border-width: 10px 0 10px 10px;
  border-color: transparent transparent transparent white;
}

/* Add arrows to the right container (pointing left) */
.right::before {
  content: " ";
  height: 0;
  position: absolute;
  top: 22px;
  width: 0;
  z-index: 1;
  left: 30px;
  border: medium solid white;
  border-width: 10px 10px 10px 0;
  border-color: transparent white transparent transparent;
}

/* Fix the circle for containers on the right side */
.right::after {
  left: -16px;
}

/* The actual content */
.content {
  padding: 20px 30px;
  background-color: [backcolor];
  position: relative;
  border-radius: 6px;
}

/* Media queries - Responsive timeline on screens less than 600px wide */
@media screen and (max-width: 600px) {
/* Place the timelime to the left */
  .timeline::after {
    left: 31px;
  }

/* Full-width containers */
  .container {
    width: 100%;
    padding-left: 70px;
    padding-right: 25px;
  }

/* Make sure that all arrows are pointing leftwards */
  .container::before {
    left: 60px;
    border: medium solid white;
    border-width: 10px 10px 10px 0;
    border-color: transparent white transparent transparent;
  }

/* Make sure all circles are at the same spot */
  .left::after, .right::after {
    left: 15px;
  }

/* Make all right containers behave like the left ones */
  .right {
    left: 0%;
  }
}</style>"""

h6=""""""


