package com.mysql.service;

import java.util.List;
import java.util.Objects;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.mysql.model.Film;
import com.mysql.repository.FilmRepository;
@Service
public class FilmServiceImpl implements FilmService {

    @Autowired
    private FilmRepository filmRepository;

    @SuppressWarnings("null")

    @Override
    public Film saveFilm(Film film) {
        return filmRepository.save(film);
    }

  @SuppressWarnings("null")
@Override
    public Film getFilmById(Long id) {
        Optional<Film> film = filmRepository.findById(id);
        if (film.isPresent()) {
            return film.get();
        }
        return null;
    }


    @Override 
    public List<Film> fetchFilmList(){
    List<Film> fetchFilmList = filmRepository.findAll();
    return fetchFilmList;   
    }

    @SuppressWarnings("null")
@Override
    public Film updateFilmById(Long id, Film film) {
        Optional<Film> film1 = filmRepository.findById(id);

        if (film1.isPresent()) {
            Film originalfilm = film1.get();

            if (Objects.nonNull(film.getTitle()) && !"".equalsIgnoreCase(film.getTitle())) {
                originalfilm.setTitle(film.getTitle());
            }
        
        return filmRepository.save(originalfilm);
}
return null;
}

    @SuppressWarnings("null")
    @Override
    public void deleteFilmById(Long id) {
        filmRepository.deleteById(id);
    }
}