/* Copy UTF-8/UTF-16/UTF-32 string.
   Copyright (C) 1999, 2002, 2006, 2009-2022 Free Software Foundation, Inc.
   Written by Bruno Haible <bruno@clisp.org>, 2002.

   This file is free software.
   It is dual-licensed under "the GNU LGPLv3+ or the GNU GPLv2+".
   You can redistribute it and/or modify it under either
     - the terms of the GNU Lesser General Public License as published
       by the Free Software Foundation, either version 3, or (at your
       option) any later version, or
     - the terms of the GNU General Public License as published by the
       Free Software Foundation; either version 2, or (at your option)
       any later version, or
     - the same dual license "the GNU LGPLv3+ or the GNU GPLv2+".

   This file is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   Lesser General Public License and the GNU General Public License
   for more details.

   You should have received a copy of the GNU Lesser General Public
   License and of the GNU General Public License along with this
   program.  If not, see <https://www.gnu.org/licenses/>.  */

UNIT *
FUNC (UNIT *dest, const UNIT *src, size_t n)
{
  for (; n > 0 && (*dest = *src) != 0; src++, dest++, n--)
    ;

  /* This behavior is rarely useful, but it is here for consistency with
     strncpy and wcsncpy.  */
  {
    UNIT *destptr = dest;

    for (; n > 0; n--)
      *destptr++ = 0;
  }

  return dest;
}
