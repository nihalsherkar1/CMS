package com.cms.services;

 

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.cms.entities.Users;
import com.cms.repository.UserRepository;

@Service
public class UserServiceImpl implements UserServices {
	
	@Autowired
	private UserRepository userRepository;

	@Override
	public Users addUser(Users user) {
		return userRepository.save(user);
	}

	public boolean validateLogin(String email,String password) {
		 Users user=userRepository.findByEmail(email);
		 return user != null && user.getPassword().equals(password);
	}
	
	public boolean  validatePassword(String password) {
		Users user=userRepository.findByPassword(password);
		return user !=null && user.getPassword().equals(password);
	}

	//Read 
	@Override
	public List<Users> fetchUsers() {	 
		return userRepository.findAll();
	}

	
	@Override
	public Optional<Users> getUserById(Long id) {
		return  userRepository.findById(id);
	}

	//update
	@Override
	public Users updateUser(Users users, Long id) {
		 Users userDb=userRepository.findById(id).get();
		 
		 if(userDb != null) {
			  userDb.setId(users.getId());
			  userDb.setName(users.getName());
			  userDb.setEmail(users.getEmail());
			  userDb.setPassword(users.getPassword());
			  userDb.setImage(users.getImage());
			  userDb.setBlog(users.getBlog());
			  userDb.setLike(users.getLike());
			  
		 } 
		return userRepository.save(userDb);
	}

	//Delete
	@Override
	public void deleteUserById(Long id) {
	 
		  userRepository.deleteById(id);
		
	}
	
	
	
	
	
	
	
	
	 
}
