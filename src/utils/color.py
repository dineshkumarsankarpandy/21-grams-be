color = '''
   {
  "theme": {
    "primaryColor": // use primary color here,
    "primaryHue":   // take Hue value of primay color 
    "primarySaturation": // take Saturation value of primary color
    "primaryLightness": // take Lightness value of primary color
  },
  "colors": {
    "surface": {
      "lightest": "hsl({theme.primaryHue}, {theme.primarySaturation}%, calc({theme.primaryLightness}% + 40%))",  //+40L
      "light": "hsl({theme.primaryHue}, {theme.primarySaturation}%, calc({theme.primaryLightness}% + 20%))",    //+20L
      "medium": "hsl({theme.primaryHue}, calc({theme.primarySaturation}% * 0.2), 45%)",        //Neutralized, L same as primary
      "dark": "hsl({theme.primaryHue}, calc({theme.primarySaturation}% * 0.2), 36%)",          //Neutralized, -10L
      "darkest": "hsl({theme.primaryHue}, calc({theme.primarySaturation}% * 0.2), 22%)"        //Neutralized, -30L
    },
    "text": {
      "primary": "hsl({theme.primaryHue}, calc({theme.primarySaturation}% * 0.2), 36%)",        //Neutralized, -10L (from surface.medium)
      "secondary": "hsl({theme.primaryHue}, calc({theme.primarySaturation}% * 0.2), 45%)",      //Neutralized, L same as primary (from surface.medium)
      "link": "hsl({theme.primaryHue}, {theme.primarySaturation}%, calc({theme.primaryLightness}% + 20%))"       //+20L (from surface.light)
    },
    "border": {
      "default": "hsl({theme.primaryHue}, calc({theme.primarySaturation}% * 0.2), 45%)",       //Neutralized, L same as primary (from surface.medium)
      "hover": "hsl({theme.primaryHue}, calc({theme.primarySaturation}% * 0.2), 58%)"         //Neutralized, +5L (from surface.medium)
    },
    "action": {
      "primary": "hsl({theme.primaryHue}, {theme.primarySaturation}%, {theme.primaryLightness}%)",      //Primary colour
      "primaryHover": "hsl({theme.primaryHue}, {theme.primarySaturation}%, calc({theme.primaryLightness}% - 10%))", //-10L (primary)
      "primaryActive": "hsl({theme.primaryHue}, {theme.primarySaturation}%, calc({theme.primaryLightness}% - 20%))",//-20L (primary)
      "secondary": "hsl({theme.primaryHue}, {theme.primarySaturation}%, calc({theme.primaryLightness}% + 10%))",  //+10L (primary)
      "secondaryHover": "hsl({theme.primaryHue}, {theme.primarySaturation}%, {theme.primaryLightness}%)"   //Primary colour
    },
    "state": {
      "success": "#2ECC40", //Example. These could also be HSL-based, shifted hue from primary.
      "warning": "#FFDC00",
      "error": "#FF4136",
      "info": "#A2D1FF"
    },
    "icon": {
      "default": "hsl({theme.primaryHue}, calc({theme.primarySaturation}% * 0.2), 45%)",     //Neutralized, L same as primary (from surface.medium)
      "informational": "#A2D1FF",
      "success": "#2ECC40",
      "warning": "#FFDC00",
      "error": "#FF4136"
    },
    "shadow": "0 0 #0000, 0 0 #0000, 0 1px 2px 0 rgba(18, 18, 23, 0.05)"
  },
  "components": {
    "formField": {
      "background": "{colors.surface.lightest}",
      "disabledBackground": "{colors.surface.medium}",
      "filledBackground": "{colors.surface.lightest}",
      "filledHoverBackground": "{colors.surface.lightest}",
      "filledFocusBackground": "{colors.surface.lightest}",
      "borderColor": "{colors.border.default}",
      "hoverBorderColor": "{colors.border.hover}",
      "focusBorderColor": "{colors.action.primary}",
      "invalidBorderColor": "{colors.state.error}",
      "color": "{colors.text.primary}",
      "disabledColor": "{colors.text.secondary}",
      "placeholderColor": "{colors.text.secondary}",
      "invalidPlaceholderColor": "{colors.surface.dark}",
      "floatLabelColor": "{colors.text.secondary}",
      "floatLabelFocusColor": "{colors.action.primaryHover}",
      "floatLabelActiveColor": "{colors.text.secondary}",
      "floatLabelInvalidColor": "{colors.surface.dark}",
      "iconColor": "{colors.text.secondary}",
      "shadow": "{colors.shadow}"
    },
    "text": {
      "color": "{colors.text.primary}",
      "hoverColor": "{colors.surface.darkest}",
      "mutedColor": "{colors.text.secondary}",
      "hoverMutedColor": "{colors.surface.dark}"
    },
    "content": {
      "background": "{colors.surface.lightest}",
      "hoverBackground": "{colors.surface.light}",
      "borderColor": "{colors.border.default}",
      "color": "{colors.text.primary}",
      "hoverColor": "{colors.surface.darkest}"
    },
    "overlay": {
      "select": {
        "background": "{colors.surface.lightest}",
        "borderColor": "{colors.border.default}",
        "color": "{colors.text.primary}"
      },
      "popover": {
        "background": "{colors.surface.lightest}",
        "borderColor": "{colors.border.default}",
        "color": "{colors.text.primary}"
      },
      "modal": {
        "background": "{colors.surface.lightest}",
        "borderColor": "{colors.border.default}",
        "color": "{colors.text.primary}"
      }
    },
    "navigation": {
      "navbar": {
        "background": "{colors.surface.darkest}",
        "color": "{colors.text.link}"
      },
      "sidebar": {
        "background": "{colors.surface.darkest}",
        "color": "{colors.text.link}"
      },
      "link": {
        "color": "{colors.text.link}",
        "hoverColor": "{colors.action.primary}",
        "activeColor": "{colors.action.primaryHover}",
        "visitedColor": "{colors.border.default}"
      },
      "dropdown": {
        "background": "{colors.surface.lightest}",
        "borderColor": "{colors.border.default}",
        "color": "{colors.text.primary}",
        "hoverBackground": "{colors.surface.light}"
      },
      "breadcrumbs": {
        "color": "{colors.text.secondary}",
        "separatorColor": "{colors.border.default}"
      }
    },
    "buttons": {
      "primary": {
        "background": "{colors.action.primary}",
        "color": "{colors.surface.lightest}",
        "hoverBackground": "{colors.action.primaryHover}",
        "activeBackground": "{colors.action.primaryActive}",
        "disabledBackground": "{colors.border.default}",
        "disabledColor": "{colors.text.secondary}"
      },
      "secondary": {
        "background": "{colors.action.secondary}",
        "color": "{colors.surface.darkest}",
        "hoverBackground": "{colors.action.primary}",
        "activeBackground": "{colors.action.primaryHover}",
        "disabledBackground": "{colors.border.default}",
        "disabledColor": "{colors.text.secondary}"
      },
      "tertiary": {
        "background": "transparent",
        "color": "{colors.action.primary}",
        "hoverBackground": "{colors.surface.light}",
        "activeBackground": "{colors.border.default}",
        "disabledBackground": "transparent",
        "disabledColor": "{colors.text.secondary}"
      },
      "ghost": {
        "background": "transparent",
        "color": "{colors.text.primary}",
        "hoverBackground": "{colors.surface.light}",
        "activeBackground": "{colors.border.default}",
        "disabledBackground": "transparent",
        "disabledColor": "{colors.text.secondary}"
      }
    },
    "cards": {
      "background": "{colors.surface.light}",
      "borderColor": "{colors.border.default}",
      "shadow": "{colors.shadow}",
      "headerColor": "{colors.text.primary}",
      "textColor": "{colors.text.primary}"
    },
    "dividers": {
      "color": "{colors.border.default}"
    },
    "alerts": {
      "success": {
        "background": "#F0F9F2",
        "borderColor": "{colors.state.success}",
        "textColor": "#194D33"
      },
      "warning": {
        "background": "#FFFBE6",
        "borderColor": "{colors.state.warning}",
        "textColor": "#665400"
      },
      "error": {
        "background": "#FDE2E1",
        "borderColor": "{colors.state.error}",
        "textColor": "#660000"
      },
      "info": {
        "background": "#EBF5FF",
        "borderColor": "{colors.state.info}",
        "textColor": "#003366"
      }
    },
    "icons": {
      "default": {
        "color": "{colors.icon.default}"
      },
      "informational": {
        "color": "{colors.icon.informational}"
      },
      "success": {
        "color": "{colors.icon.success}"
      },
      "warning": {
        "color": "{colors.icon.warning}"
      },
      "error": {
        "color": "{colors.icon.error}"
      }
    },
    "footer": {
      "background": "{colors.surface.darkest}",
      "color": "{colors.text.link}",
      "link": {
        "color": "{colors.action.primary}",
        "hoverColor": "{colors.action.primaryHover}"
      }
    }
  },
  "usage_guidelines": {
    "neutral_palette_usage": {
      "surface.lightest": "Use for the lightest background, typically the main page background. ",
      "surface.container": "Apply to container backgrounds, section dividers, and subtle UI areas.",
      "surface.card": "Use for card backgrounds.",
      "border.default": "Apply to borders and dividers.",
      "border.secondary": "Use for secondary borders and disabled UI elements.",
      "input": "Apply to input fields and muted UI elements.",
      "text.secondary": "Use for secondary text, labels, and low-emphasis icons.",
      "text.primary_on_light": "Apply for primary text on light backgrounds.",
      "text.high_emphasis": "Use for high-emphasis text and strong UI elements.",
      "surface.dark": "Apply to dark backgrounds, including cards, panels, and modals.",
      "surface.darkest": "Use for the darkest backgrounds, such as the navigation bar and side panels."
    },
    "brand_palette_usage": {
      "action.primary": "Use as the lightest tint for background highlights.",
      "highlight": "Apply to subtle UI highlights and soft background accents.",
      "hover_states": "Use for hover states and selected items' backgrounds.",
      "cta_secondary": "Apply to secondary CTA backgrounds.",
      "cta_primary": "Use for primary CTAs and active elements.",
      "button_pressed": "Apply for active button pressed states and emphasized UI.",
      "focused_elements": "Use for focused elements and high-impact UI.",
      "contrast_elements": "Apply a darker primary color for contrast elements.",
      "strong_emphasis": "Use the deepest primary shade for strong emphasis."
    },
    "accent_colors_usage": {
      "error": "Use for error states, alerts, and validation messages.",
      "success": "Apply to success indicators and positive actions.",
      "warning": "Use for caution areas and warnings.",
      "info": "Apply to notifications and informational messages.",
      "interactive": "Use for hover, active, and focus states.",
      "cta_secondary": "Apply to secondary button backgrounds.",
      "ui_indicator": "Use for subtle UI highlights and status indicators."
    },
    "implementation_guidelines": {
      "neutral": "Use 60% Neutral Colors for backgrounds, containers, and text.",
      "brand": "Use 30% Brand Colors for key UI elements like buttons and section dividers.",
      "accent": "Use 10% Accent Colors for alerts, notifications, and interactive elements."
    }
  }
}




'''