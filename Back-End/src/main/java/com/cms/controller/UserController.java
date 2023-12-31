package com.cms.controller;

 
 
import java.util.List;
import java.util.Map;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RequestPart;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import com.cms.entities.Users;
import com.cms.services.UserServiceImpl;

 
@RestController
@RequestMapping("/cms/usercontroller")
public class UserController {

	@Autowired
	private UserServiceImpl serviceImpl;
	
	@PostMapping("/add")
	public ResponseEntity<Users> addUser(  @RequestPart("image") MultipartFile file,
	        @RequestParam("name") String name,
	        @RequestParam("email") String email,
	        @RequestParam("password") String password  ) {
		    
		try {
			 byte[] imageData = file.getBytes();
			 Users user = new Users();
			 user.setName(name);
		        user.setEmail(email);
		        user.setPassword(password);
		        user.setImage(imageData);
		        Users result = serviceImpl.addUser(user);
		    System.out.println( result.getImage());	     	  		    
		    if(result.getName() == null || result.getEmail()==null || result.getPassword()== null  ) {
		    	   return new  ResponseEntity<>(result,HttpStatus.UNAUTHORIZED);
		    }else {
		   	 return new ResponseEntity<>(result,HttpStatus.CREATED);
		    }	 		 
		} catch (Exception e) {
			return new ResponseEntity<Users>(HttpStatus.INTERNAL_SERVER_ERROR);
		}
		
	}
	 
	@PostMapping("/login")
	public ResponseEntity<String> loginUser(@RequestBody Map<String, String> loginData) {
	    try {
	        String email = loginData.get("email");
	        String password = loginData.get("password");         
	        boolean isValidLogin = serviceImpl.validateLogin(email, password);
	        boolean isPassword=serviceImpl.validatePassword(password);        	      	
	        if (isValidLogin && isPassword) {
	            return new ResponseEntity<>("Login Successful", HttpStatus.OK);
	        } else {
	            return new ResponseEntity<>("Invalid email or password", HttpStatus.UNAUTHORIZED);
	        }
	    } catch (Exception e) {
	        return new ResponseEntity<>("Internal Server Error", HttpStatus.INTERNAL_SERVER_ERROR);
	    }
	}
	
	//Read 
	    @GetMapping("/allusers")
		public List<Users> fetchUsers() {	 
			return serviceImpl.fetchUsers();
		}

	    //Get only one user by using id
	    public Optional<Users> getUserById(Long id) {
			return serviceImpl.getUserById(id) ;
		}
	    
	    
		//update
	 
	    @PutMapping("/user/{id}")
		public Users updateUser( @RequestBody Users users, @PathVariable("id")  Long id) { 
			return serviceImpl.updateUser(users, id);
		}

		//Delete
		 @DeleteMapping("/user/{id}")
		public String deleteUserById( @PathVariable Long id) {
		 
			  serviceImpl.deleteUserById(id);
			  return "Deleted SuccessFully";
			
		}
		
	
	
	
	
	
	
	
	

}
