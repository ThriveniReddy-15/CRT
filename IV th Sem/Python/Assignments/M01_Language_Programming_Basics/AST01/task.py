def Ticket_Pricing(n: int) -> int:
      if n < 10:
         return 10
      elif n % 10 == 0:
         return 15
      else:
         return 20


if __name__ == '__main__':
    n = int(input())
    print(Ticket_Pricing(n))
