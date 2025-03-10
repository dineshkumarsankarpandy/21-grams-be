layout = """
``html

     <style>
 /* Reset some default styles for consistency */
body, h1, h2, p, img {
  margin: 0;
  padding: 0;
  border: 0;
  font-size: 100%;
  font: inherit;
  vertical-align: baseline;
  box-sizing: border-box; /* Important for padding and border calculation */
}

img {
  max-width: 100%; /* Ensure images don't overflow their containers */
  height: auto;
  display: block; /* Remove extra space below images */
}


/* --- General Section Styles --- */
.section {
  overflow: hidden; /* Handles potentially overflowing content */
}

.padding-global {
  /* Define global padding - adjust values as needed */
  padding-left: 20px;
  padding-right: 20px;

}

.padding-section-xlarge {
  padding-top: 80px;
  padding-bottom: 80px;
}

.inclusion { /* Combines both padding classes */
  /* Inherits from padding-global and padding-section-xlarge */
}

.container-large {
  max-width: 1200px; /*  Adjust as needed for desired container width */
  margin: 0 auto;      /* Center the container horizontally */
  padding-left: 20px;  /* Match padding-global for consistent spacing */
  padding-right: 20px;
}

/* --- Heading Styles --- */
.heading-wrap_wide-flex {
  margin-bottom: 40px; /* Space between heading and content */
}

.heading-style-h2 {
  font-size: 2.5em;    /*  Adjust as needed  */
  line-height: 1.2;
  font-weight: bold;    /*  Adjust as needed  */
  color: #121a21;      /*  Match branding color  */
}

/* --- Inclusion Specific Styles --- */

.inclusion_wrap {
    display: flex;
    flex-direction: column; /* Stack collage and description */
    gap: 30px; /* Space between collage and description */
}


.inclusion-collage-wrap {
  display: flex;
  flex-wrap: wrap; /* Allow images to wrap to the next line */
  justify-content: flex-start; /* Align items to the start */
  gap: 10px;           /* Space between images */
}

.inclusion-img_wrap {
  width: calc(50% - 5px);  /* Two images per row with gap */
  /* Or, use a fixed width if desired:  width: 200px; */
  overflow: hidden; /* Crop any overflowing image */
  border-radius: 5px; /* Optional: Rounded corners */
}


/* You might need to adjust this breakpoint based on your design */
@media (min-width: 768px) {
    .inclusion-collage-wrap {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); /* Responsive grid */
      gap: 10px;
    }
    .inclusion-img_wrap {
        width: auto; /*Let grid handle image sizes*/
    }
}


.inclusion-img {
  width: 100%;        /* Image fills its container */
  height: auto;
  object-fit: cover;  /* Maintain aspect ratio and cover the area */
  display: block;
}

.inclusion-description-wrap-s {
  /* Styles for the description container, if needed */
}

.text-size-large {
  font-size: 1.2em;    /*  Adjust as needed  */
  line-height: 1.6;
  color: #121a21;      /*  Match branding color  */
}

/* --- Utility Classes (Optional) --- */

.overflow-hidden {
  overflow: hidden;
}

/* Image Style Classes */
.img-style-1 {
    border-top-left-radius: 11.875rem;
    border-bottom-left-radius: 0;
}

.img-style-2 {
    border-top-right-radius: 11.875rem;
    border-bottom-right-radius: 0;
}

.img-style-3 {
    border-bottom-left-radius: 11.875rem;
    border-top-left-radius: 0;
}

.img-style-4 {
    border-bottom-right-radius: 11.875rem;
    border-top-right-radius: 0;
}

/* Example responsive adjustments */
@media (max-width: 767px) {
  .heading-style-h2 {
    font-size: 2em; /* Smaller heading on smaller screens */
  }
  .text-size-large {
    font-size: 1em; /* Smaller text on smaller screens */
  }
  .padding-section-xlarge {
    padding-top: 60px;
    padding-bottom: 60px;
  }
}

@media (max-width: 479px) {
  .heading-style-h2 {
    font-size: 1.75em; /* Even smaller heading on very small screens */
  }
}

     </style>



    <section class="section overflow-hidden">
  <div class="padding-global padding-section-xlarge inclusion">
    <div class="container-large">
      <div class="heading-wrap_wide-flex">
        <h2 class="heading-style-h2">
          Inclusion in<br>the workplace
        </h2>
      </div>
      <div class="inclusion_wrap">
        <div class="inclusion-collage-wrap">
          <div class="inclusion-img_wrap img-style-1">
            <img
              loading="lazy"
              sizes="(max-width: 479px) 44vw, (max-width: 767px) 46vw, 191.9957275390625px"
              srcset="
                https://cdn.prod.website-files.com/660c66ade713b40a25c5f897/661d4b13f1317a83ebc7ad77_Rectangle%20333%20(1)-p-500.jpg   500w,
                https://cdn.prod.website-files.com/660c66ade713b40a25c5f897/661d4b13f1317a83ebc7ad77_Rectangle%20333%20(1).jpg   768w
              "
              alt=""
              class="inclusion-img"
              src="https://cdn.prod.website-files.com/660c66ade713b40a25c5f897/661d4b13f1317a83ebc7ad77_Rectangle%20333%20(1).jpg"
            >
          </div>
          <div class="inclusion-img_wrap img-style-2">
            <img
              loading="lazy"
              sizes="(max-width: 479px) 44vw, (max-width: 767px) 46vw, 191.9957275390625px"
              srcset="
                https://cdn.prod.website-files.com/660c66ade713b40a25c5f897/661d4b134a12ab4ef1c2bf8b_Rectangle%20332%20(1)-p-500.jpg   500w,
                https://cdn.prod.website-files.com/660c66ade713b40a25c5f897/661d4b134a12ab4ef1c2bf8b_Rectangle%20332%20(1).jpg   768w
              "
              alt=""
              class="inclusion-img"
              src="https://cdn.prod.website-files.com/660c66ade713b40a25c5f897/661d4b134a12ab4ef1c2bf8b_Rectangle%20332%20(1).jpg"
            >
          </div>
          <div class="inclusion-img_wrap img-style-3">
            <img
              loading="lazy"
              sizes="(max-width: 479px) 44vw, (max-width: 767px) 46vw, 191.9957275390625px"
              srcset="
                https://cdn.prod.website-files.com/660c66ade713b40a25c5f897/661d4b13bd1843b4ec6e9c21_Rectangle%20330%20(1)-p-500.jpg   500w,
                https://cdn.prod.website-files.com/660c66ade713b40a25c5f897/661d4b13bd1843b4ec6e9c21_Rectangle%20330%20(1).jpg   768w
              "
              alt=""
              class="inclusion-img"
              src="https://cdn.prod.website-files.com/660c66ade713b40a25c5f897/661d4b13bd1843b4ec6e9c21_Rectangle%20330%20(1).jpg"
            >
          </div>
          <div class="inclusion-img_wrap img-style-4">
            <img
              loading="lazy"
              sizes="(max-width: 479px) 44vw, (max-width: 767px) 46vw, 191.9957275390625px"
              srcset="
                https://cdn.prod.website-files.com/660c66ade713b40a25c5f897/661d4b13fa8d01daa6bba196_Rectangle%20331%20(1)-p-500.jpg   500w,
                https://cdn.prod.website-files.com/660c66ade713b40a25c5f897/661d4b13fa8d01daa6bba196_Rectangle%20331%20(1).jpg   768w
              "
              alt=""
              class="inclusion-img"
              src="https://cdn.prod.website-files.com/660c66ade713b40a25c5f897/661d4b13fa8d01daa6bba196_Rectangle%20331%20(1).jpg"
            >
          </div>
        </div>
        <div class="inclusion-description-wrap-s">
          <p class="text-size-large">
            For us, Diversity and Inclusivity isn’t just a box-ticking exercise.
            We are committed to supporting and celebrating diversity for all
            colleagues, all year round. It’s part of our culture. It always
            has been and always will be. Because accepting people for who they
            are is simply the right thing to do.
          </p>
        </div>
      </div>
    </div>
  </div>
</section>





    """
