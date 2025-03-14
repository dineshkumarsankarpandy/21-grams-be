user_profile_photos= {
                  "https://cdn.prod.website-files.com/660c66ade713b40a25c5f897/661d4b13f1317a83ebc7ad77_Rectangle%20333%20(1).jpg",
                  "https://cdn.prod.website-files.com/660c66ade713b40a25c5f897/661d4b134a12ab4ef1c2bf8b_Rectangle%20332%20(1).jpg",
                  "https://cdn.prod.website-files.com/660c66ade713b40a25c5f897/661d4b13bd1843b4ec6e9c21_Rectangle%20330%20(1).jpg",
                  "https://cdn.prod.website-files.com/660c66ade713b40a25c5f897/661d4b13fa8d01daa6bba196_Rectangle%20331%20(1).jpg"
                
                }







          


logos = {
  
    "https://cdn.prod.website-files.com/66e88746834b80507cdf7933/66e8a82d52566d454c99501c_Discord.svg",
    "https://cdn.prod.website-files.com/66e88746834b80507cdf7933/66e8a82d52566d454c994fcd_NCR.svg",
    "https://cdn.prod.website-files.com/66e88746834b80507cdf7933/67c9bb1d7c6fbfb04e6aec52_spotify.svg",
    "https://cdn.prod.website-files.com/66e88746834b80507cdf7933/66e8a82b52566d454c994910_mondaycom.svg",
    "https://cdn.prod.website-files.com/66e88746834b80507cdf7933/66e8a82d52566d454c994fdb_Ted.svg",
    "https://cdn.prod.website-files.com/66e88746834b80507cdf7933/66e8a82d52566d454c994fba_Dropbox.svg",
    "https://cdn.prod.website-files.com/66e88746834b80507cdf7933/6708139d2e30eb81beb54cc7_orangetheory-logo.svg",
    "https://cdn.prod.website-files.com/66e88746834b80507cdf7933/66e8a82d52566d454c994fb6_Greenhouse.svg",
    "https://cdn.prod.website-files.com/66e88746834b80507cdf7933/67c9bb1d4f490d1737bd541b_clear-light.svg",
    "https://cdn.prod.website-files.com/66e88746834b80507cdf7933/67c9bb1d3a2b2a689e41db67_soundcloud.svg",
    "https://cdn.prod.website-files.com/66e88746834b80507cdf7933/67c9bb1d077ff1ae73acf7ce_Mizuho.svg",
    "https://cdn.prod.website-files.com/66e88746834b80507cdf7933/67c9bb1d6631a163fd6f49a7_checkout.svg",
    "https://cdn.prod.website-files.com/66e88746834b80507cdf7933/66e8a82e52566d454c99502c_ideo-logo.svg",
    "https://cdn.prod.website-files.com/66e88746834b80507cdf7933/67c9bb1282a2e5ddf6306d15_docusign.svg",
    "https://cdn.prod.website-files.com/66e88746834b80507cdf7933/66e8a82d52566d454c994fd1_Mural.svg",
    "https://cdn.prod.website-files.com/66e88746834b80507cdf7933/66e8a82e52566d454c995044_Name%3DABM%20Industries%2C%20Mode%3DLight.svg",
    "https://cdn.prod.website-files.com/66e88746834b80507cdf7933/66e8a82e52566d454c995028_TheNewYorkTimes.svg",
    "https://cdn.prod.website-files.com/66e88746834b80507cdf7933/66e8a82c52566d454c994f5e_Upwork.svg",
    "https://cdn.prod.website-files.com/66e88746834b80507cdf7933/66e8a82e52566d454c995054_Decathlon.svg",
    
}





implementation_step = '''

                           <div id="logo-container" class="grid grid-cols-3 gap-4">
  <!-- Logos will be injected here -->
</div>

<script>
  const logoData = {
    "logos": [
      "https://cdn.prod.website-files.com/66e88746834b80507cdf7933/66e8a82d52566d454c99501c_Discord.svg",
      "https://cdn.prod.website-files.com/66e88746834b80507cdf7933/66e8a82d52566d454c994fcd_NCR.svg",
      "https://cdn.prod.website-files.com/66e88746834b80507cdf7933/67c9bb1d7c6fbfb04e6aec52_spotify.svg",
      "https://cdn.prod.website-files.com/66e88746834b80507cdf7933/66e8a82b52566d454c994910_mondaycom.svg",
      "https://cdn.prod.website-files.com/66e88746834b80507cdf7933/66e8a82d52566d454c994fdb_Ted.svg",
      "https://cdn.prod.website-files.com/66e88746834b80507cdf7933/66e8a82d52566d454c994fba_Dropbox.svg"
    ]
  };

  const container = document.getElementById("logo-container");

  logoData.logos.forEach(logoUrl => {
    const img = document.createElement("img");
    img.src = logoUrl;
    img.alt = "Company Logo";
    img.classList.add("w-24", "h-auto", "filter", "brightness-0"); // Apply black color filter
    container.appendChild(img);
  });
</script>

<style>
  img {
    filter: brightness(0); /* Ensures all logos turn black */
  }
</style>



                     '''




