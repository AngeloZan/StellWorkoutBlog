def posts_matrix(posts):
    # receives a list of post objects and sorts them in a 3x3 matrix
    mtx = [ [], ]

    for post in posts:
        if len(mtx[0]) < 3:
            mtx[0].insert(0, post)
        else:
            mtx.insert(0, [post])

    mtx.reverse()
    
    for line in mtx:
        line.reverse()

    return mtx
