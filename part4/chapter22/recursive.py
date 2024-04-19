def recursive(bob):
    if bob < 1:
        print(
            """
              No more bottles of beer on the wall.
              No more bottles of beer.
              """
        )
        return

    tmp = bob
    bob -= 1
    print(
        f"""{tmp} bottles of beer on the wall.
          {tmp} bottles of beer.
          Take one down, pass it around,
          {bob} bottles of beer on the wall.
          """
    )
    recursive(bob)


recursive(99)
