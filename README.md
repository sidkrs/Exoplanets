# Exoplanets
Finds the Planet Most Similar To Earth in the Discovered Universe

- Takes in the CSV file from: "https://github.com/OpenExoplanetCatalogue/open_exoplanet_catalogue" which is a regularly updated list
  of all exoplanets discovered by scientists with their unique specifications_ids: name, mass, radius, period, semimajoraxis, eccentricity, 
  longitude, temperature, age, discoverymethod, and discoveryyear
  
- Uitilzaed a custom Euclid formula that measured the change in mass, radius, period, surface temperature, and semimajor axis compared
  earth.
- ((Δ Mass)^2 +(Δ Radius)^2 +(Δ Period)^2 +(Δ SemimajorAxis)^2 +(Δ SurfaceTemp)^2)^1/2


