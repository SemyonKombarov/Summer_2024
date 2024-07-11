def tower(n,s1,s2,s3):
    if n > 0 :
        tower(n-1,s1,s3,s2)
        print(f'Disk №{n} from {s1} to {s2}')
        tower(n-1,s3,s2,s1)

tower(3,"S1",'S2','S3')
