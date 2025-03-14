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


blockquote_layout = '''
                                       <section>
                                        <div>
                                        <figure>
                                            <blockquote>
                                            <span>Figma brings together designers, project managers, product managers, and engineers. The quality of feedback is 10x better.</span>
                                            </blockquote>
                                            <div class=" ">
                                            <figcaption>
                                                <p>Shawn Lam, Head of Design, Zoom</p>
                                            </figcaption>
                                            <img width="160" height="66" alt="zoom logo" src="https://cdn.sanity.io/images/599r6htc/regionalized/55849a17b1f1c0e4b6844dc94c257e25ce68d8c9-156x64.svg?q=75&amp;fit=max&amp;auto=format">
                                            </div>
                                        </figure>
                                        </div>
                                    </section>  

                                     blockquote {
                                            font-family:'Times New Roman', Times, serif;
                                            font-size: 3.2rem;
                                            font-style: italic;
                                            color: #333;
                                            border-left: 4px solid #0073e6;
                                            padding-left: 1.5rem;
                                            max-width: 45ch;
                                        }
 
                                    figcaption {
                                      font-family: semi-bold;
                                      font-size: 2rem;
                                      color: #555;
                                    }
                                
                                    .grid{
                                        grid-template-rows: auto;
                                
                                    }


'''


grid_layout = """

      {
  "ai_agent_instructions": {
    "start": {
      "identify_context": [
        "Detect device & viewport size",
        "Analyze content type (Text, Images, Data, Mixed, Ecommerce, Dashboard, Form-based UI, etc.)",
        "Extract user behavior insights (Eye-tracking, Click heatmaps, Scroll-depth)",
        "Check accessibility requirements (WCAG compliance, contrast, keyboard navigation)"
      ],
      "decision_triggers": [
        "If text-heavy → Use Baseline Grid",
        "If image-heavy → Use Masonry or Modular Grid",
        "If data-driven → Use Bento Grid or Card-based Grid",
        "If mixed content → Use Asymmetric or 12-column Grid",
        "If ecommerce → Use 4-5 column Grid with product cards",
        "If dashboard → Use Card-based Grid or Bento Grid for modular sections",
        "If form-based UI → Use Single-column or Multi-step Grid",
        "If storytelling UI → Use Asymmetric or Freeform Grid",
        "If complex analytics UI → Use Flexible Modular Grid with nested sections"
      ],
      "fallback_strategy": "Default to 12-column Grid with auto-adaptive behavior if no clear match is found"
    },
    "adaptive_behavior": {
      "viewport_changes": {
        "mobile": "1-column layout",
        "tablet": "2-3 column layout",
        "desktop": "4-6 column layout",
        "large_screens": "Responsive multi-column with max-width handling"
      },
      "dynamic_content": {
        "auto_reflow": true,
        "animation": "smooth-transition"
      },
      "wcag_adaptation": {
        "touch_target_minimum": "44px",
        "contrast_ratio": "4.5:1 minimum",
        "keyboard_navigation": true
      }
    },
    "grid_selection_logic": {
      "text_heavy": "Baseline Grid",
      "image_heavy": "Masonry or Modular Grid",
      "data_driven": "Bento Grid or Card-based Grid",
      "ecommerce": "4-5 column Grid with adaptive card sizes",
      "landing_page": "Asymmetric or 12-column Grid",
      "dashboard": "Card-based Grid with nested modular sections",
      "form_ui": "Single-column Grid for focus & Multi-step Grid for user journey",
      "storytelling_ui": "Asymmetric or Freeform Grid for creative layouts",
      "analytics_dashboard": "Flexible Modular Grid with hierarchical data layout",
      "hybrid_grid_decision": "AI dynamically selects grids for sections with mixed content"
    },
    "hybrid_grids": {
      "header": "Full-width or Asymmetric Grid",
      "body": "12-column or Flexible Modular Grid",
      "sidebar": "Fixed Column Grid",
      "footer": "Baseline Grid for alignment"
    },
    "user_behavior_analysis": {
      "eye_tracking": {
        "hotspot_zones": ["top-left", "center", "F-pattern", "Z-pattern"],
        "adjust_grid_weight": true
      },
      "interaction_data": {
        "click_density": "high",
        "scroll_depth": "moderate",
        "preferred_layout": "masonry_grid or card_grid based on engagement"
      },
      "adaptive_ui": {
        "personalized_grids": true,
        "history_based_suggestions": true
      }
    },
    "machine_learning": {
      "train_on_user_data": true,
      "feedback_loop": "Adjust grid selection based on user engagement",
      "dataset": "Historical layout performance"
    },
    "component_placement": {
      "hero_section": "Full-width Asymmetric Grid",
      "product_list": "Masonry Grid for dynamic image sizes",
      "form_section": "Single-column Grid for user focus",
      "dashboard_cards": "Card-based Grid with nested sections",
      "navigation_menu": "Fixed or Flexbox Grid",
      "feature_highlight": "Modular Grid with emphasized focus",
      "testimonials_section": "Carousel or 3-column Grid",
      "pricing_table": "4-column or Card-based Grid",
      "blog_list": "Masonry or Card Grid",
      "gallery": "Masonry or Modular Grid",
      "call_to_action": "Full-width Centered Grid",
      "footer_links": "Baseline or Multi-column Grid",
      "sidebar_widgets": "Fixed Column or Flexible Grid",
      "search_results": "Card Grid or List View with filtering",
      "user_profile": "Two-column layout with a sidebar",
      "notifications": "Stacked Grid or Dropdown",
      "checkout_page": "Multi-step or Single-column Grid",
      "error_pages": "Centered Grid with prominent messaging"
    },
    "decision_flow": [
      "Detect device & viewport size",
      "Analyze content type",
      "Map to the best-fit grid",
      "Adjust based on user interaction",
      "Apply real-time changes",
      "Check accessibility compliance",
      "Output a framework-specific implementation"
    ],
    "framework_integration": {
      "bootstrap": { "grid_type": "12-column", "class": "row-cols-auto", "supports_flex": true },
      "tailwind_css": { "grid_type": "CSS Grid/Flexbox", "class": "grid-cols-12", "supports_auto_layout": true },
      "material_ui": { "grid_type": "Container/Grid Item", "class": "spacing-system", "supports_breakpoints": true }
    },
    "experimental_layouts": {
      "AI_generated_grids": "Dynamic grid systems that adapt based on past user engagement and real-time content analysis",
      "3D_ui_support": "Experimental grid structures for immersive design environments"
    },
    "end": {
      "final_output": {
        "optimized_grid": "Best-matched grid based on content & user data",
        "ui_flexibility": "Ensuring adaptability for future changes",
        "code_snippets": "Provide ready-to-use grid code"
      }
    }
  }
}

"""