var facts = ["the average student in grades 3-8 who took a math assessment this fall scored 5 to 10 percentile points behind students who took the same test last year", "There is a need to ameliorate children and adolescents’ access to mental health support services geared towards providing measures for developing healthy coping mechanisms during the current crisis", "there were a number of children that were unable to get medical attention from their doctors since their parents lost insurence due to losing their job during the pandemic"]
var randomFact = randomlist(facts);

function generateFacts() {
  document.getElementById('here').innerHTML = randomFact;
}

function randomlist(list) {
  var x = Math.floor(Math.random() * list.length);
  return list[x];
}
