package com.mysql.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import com.mysql.model.Film;


@Repository
public interface FilmRepository extends JpaRepository<Film , Long> {

    Object findAllById(Long id);
   
}
