def posts_matrix(posts):
    # receives a list of post objects and sorts them in a 3x3 matrix
    mtx = [ [], ]

    for post in posts:
        if len(mtx[-1]) < 3:
            mtx[-1].append(post)
        else:
            mtx.append([post])

    return mtx
