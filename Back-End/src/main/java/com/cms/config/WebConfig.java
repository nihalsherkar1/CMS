package com.cms.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
@EnableWebMvc  
public class WebConfig implements WebMvcConfigurer {

	@Override
	public void addCorsMappings(CorsRegistry registry) {
		 registry.addMapping("/cms/usercontroller/**")
	 
		 .allowedOriginPatterns("http://127.0.0.1:5500")
		  .allowedMethods("GET","POST","PUT","DELETE")
		  .allowedHeaders("*")
		  .allowCredentials(true)
		  .maxAge(3600)  // Max age of the preflight request in seconds
		  ;
		  

		 
	}

	
	
}
